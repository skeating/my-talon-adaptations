from talon import Module, actions


mod = Module()


@mod.action_class
class Actions:
    def good_morning():
        """ starts all the applications I need for my day"""
        actions.user.switcher_launch("com.squirrel.slack.slack")
        actions.user.switcher_launch("chrome")

    