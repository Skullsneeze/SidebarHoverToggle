import sublime, sublime_plugin

class SidebarToggleListener(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        # to not raise an AttributeError Exception
        # I check if the attribute exists (in both function)
        if not hasattr(self, 'disable_auto_show'):
            self.disable_auto_show = False
        # if the auto show is disable, stop everything
        if self.disable_auto_show:
            return

        if hover_zone == sublime.HOVER_GUTTER:
            # hover over gutter. open the sidebar
            view.window().set_sidebar_visible(True)
        else:
            # hide sidebar
            view.window().set_sidebar_visible(False)

    def on_window_command(self, window, command, args):
        """ listen for every window_command. The one that matters here is `toggle_side_bar` """
        if not hasattr(self, 'disable_auto_show'):
            self.disable_auto_show = False

        if command != 'toggle_side_bar':
            return
        # the side bar is hidden, but because this function is fired
        # before the command is run, the side bar is going to be in the *opposite*
        # state than now
        is_going_to_be_visisble = not window.is_sidebar_visible()
        # if this condition is true, it means that the user showed the side bar manually
        # so we disable auto hide/show
        if is_going_to_be_visisble is True:
            self.disable_auto_show = True
        else:
            self.disable_auto_show = False
