from talon import Module, actions


mod = Module()


@mod.action_class
class Actions:
    def start_lib_programming():
        """ starts all the applications I need for programming libSBML"""
        actions.user.switcher_launch("com.squirrel.gitkraken.gitkraken")
        actions.user.switcher_launch("VisualStudio.5d342c33")
        actions.user.switcher_launch("{6D809377-6AF0-444B-8957-A3773F02200E}\CMake\\bin\cmake-gui.exe")
