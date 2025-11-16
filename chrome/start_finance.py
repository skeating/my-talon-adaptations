from talon import Module, actions


mod = Module()


@mod.action_class
class Actions:
    def start_finance():
        """ starts all the applications I need for my finance"""
        actions.user.switcher_launch("Microsoft.Office.EXCEL.EXE.15")    

    def start_emap_programming():
        """ starts all the applications for programming EMAP"""
        actions.user.switcher_launch("com.squirrel.gitkraken.gitkraken")
        actions.user.switcher_launch("IO Microsoft.VisualStudioCode")
        actions.user.switcher_launch("IO {6D809377-6AF0-444B-8957-A3773F02200E\\JetBrains\\IntelliJ IDEA Community Edition 2025.1.4.1\\bin\\idea64.exe")