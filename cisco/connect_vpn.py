from talon import Module, actions


mod = Module()


@mod.action_class
class Actions:
    def connect_vpn():
        """ starts all the applications I need for my ^day"""
        actions.user.switcher_launch("Cisco.AnyConnect")
        