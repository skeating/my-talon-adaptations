from talon import Module, actions


mod = Module()


@mod.action_class
class Actions:
    def start_finance():
        """ starts all the applications I need for my finance"""
        actions.user.switcher_launch("Microsoft.Office.EXCEL.EXE.15")    

