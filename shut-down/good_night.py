import os
import shlex
import subprocess
import time
from pathlib import Path

import talon
from talon import Module, Context, ui, app, actions

mod = Module()
mod.list("running", desc="all running applications")
ctx = Context()

# a list of the current overrides
overrides = {}

# apps to exclude from running list
excludes = set()

# a list of the currently running application names
running_application_dict = {}

words_to_exclude = [
    "zero",
    "one",
    "two",
    "three",
    "for",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "and",
    "dot",
    "exe",
    "help",
    "install",
    "installer",
    "microsoft",
    "nine",
    "readme",
    "studio",
    "terminal",
    "visual",
    "windows",
]

# on Windows, WindowsApps are not like normal applications, so
# we use the shell:AppsFolder to populate the list of applications
# rather than via e.g. the start menu. This way, all apps, including "modern" apps are
# launchable. To easily retrieve the apps this makes available, navigate to shell:AppsFolder in Explorer
if app.platform == "windows":
    import ctypes
    import os

    import pywintypes

    try:
        pass
    except ImportError:
        # Python 2
        pass

        bytes = lambda x: str(buffer(x))

    from ctypes import wintypes

    from win32com.propsys import propsys, pscon
    from win32com.shell import shell, shellcon

    # KNOWNFOLDERID
    # https://msdn.microsoft.com/en-us/library/dd378457
    # win32com defines most of these, except the ones added in Windows 8.
    FOLDERID_AppsFolder = pywintypes.IID("{1e87508d-89c2-42f0-8a7e-645a0f50ca58}")

    # win32com is missing SHGetKnownFolderIDList, so use ctypes.

    _ole32 = ctypes.OleDLL("ole32")
    _shell32 = ctypes.OleDLL("shell32")

    _REFKNOWNFOLDERID = ctypes.c_char_p
    _PPITEMIDLIST = ctypes.POINTER(ctypes.c_void_p)

    _ole32.CoTaskMemFree.restype = None
    _ole32.CoTaskMemFree.argtypes = (wintypes.LPVOID,)

    _shell32.SHGetKnownFolderIDList.argtypes = (
        _REFKNOWNFOLDERID,  # rfid
        wintypes.DWORD,  # dwFlags
        wintypes.HANDLE,  # hToken
        _PPITEMIDLIST,
    )  # ppidl

    def get_known_folder_id_list(folder_id, htoken=None):
        if isinstance(folder_id, pywintypes.IIDType):
            folder_id = bytes(folder_id)
        pidl = ctypes.c_void_p()
        try:
            _shell32.SHGetKnownFolderIDList(folder_id, 0, htoken, ctypes.byref(pidl))
            return shell.AddressAsPIDL(pidl.value)
        except OSError as e:
            if e.winerror & 0x80070000 == 0x80070000:
                # It's a WinAPI error, so re-raise it, letting Python
                # raise a specific exception such as FileNotFoundError.
                raise ctypes.WinError(e.winerror & 0x0000FFFF)
            raise
        finally:
            if pidl:
                _ole32.CoTaskMemFree(pidl)

    def enum_known_folder(folder_id, htoken=None):
        id_list = get_known_folder_id_list(folder_id, htoken)
        folder_shell_item = shell.SHCreateShellItem(None, None, id_list)
        items_enum = folder_shell_item.BindToHandler(
            None, shell.BHID_EnumItems, shell.IID_IEnumShellItems
        )
        yield from items_enum

    def list_known_folder(folder_id, htoken=None):
        result = []
        for item in enum_known_folder(folder_id, htoken):
            result.append(item.GetDisplayName(shellcon.SIGDN_NORMALDISPLAY))
        result.sort(key=lambda x: x.upper())
        return result

    def get_windows_apps():
        items = {}
        for item in enum_known_folder(FOLDERID_AppsFolder):
            try:
                property_store = item.BindToHandler(
                    None, shell.BHID_PropertyStore, propsys.IID_IPropertyStore
                )
                app_user_model_id = property_store.GetValue(
                    pscon.PKEY_AppUserModel_ID
                ).ToString()

            except pywintypes.error:
                continue

            name = item.GetDisplayName(shellcon.SIGDN_NORMALDISPLAY)

            # exclude anything with install/uninstall...
            # 'cause I don't think we don't want 'em
            if "install" not in name.lower():
                items[name] = app_user_model_id

        return items


def update_running_list():
    global running_application_dict
    running_application_dict = {}
    running = {}
    foreground_apps = ui.apps(background=False)

    print("here I am")

    for cur_app in foreground_apps:
        running_application_dict[cur_app.name.lower()] = cur_app.name

        if app.platform == "windows":
            exe = os.path.basename(cur_app.exe)
            running_application_dict[exe.lower()] = exe

    override_apps = excludes.union(overrides.values())

    running = actions.user.create_spoken_forms_from_list(
        [
            curr_app.name
            for curr_app in ui.apps(background=False)
            if curr_app.name.lower() not in override_apps
            and curr_app.exe.lower() not in override_apps
            and os.path.basename(curr_app.exe).lower() not in override_apps
        ],
        words_to_exclude=words_to_exclude,
        generate_subsequences=True,
    )

    for running_name, full_application_name in overrides.items():
        if running_app_name := running_application_dict.get(full_application_name):
            running[running_name] = running_app_name

    ctx.lists["self.running"] = running

@mod.action_class
class Actions:
    def good_night():
        """closes all open applications"""
        print("good night everybody")
        for app in ctx.lists["self.running"]:
            actions.switcher_focus_app(app)
            actions.key("alt-f4")
        
        
