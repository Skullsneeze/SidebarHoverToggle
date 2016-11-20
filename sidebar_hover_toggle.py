import sublime, sublime_plugin

class SidebarToggleListener(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        if not hasattr(self, 'disable_auto_show'):
            self.disable_auto_show = False

        if self.disable_auto_show:
            return

        if hover_zone == sublime.HOVER_GUTTER:
            # hover over gutter. open the sidebar
            view.window().set_sidebar_visible(True)
        else:
            # hide sidebar
            view.window().set_sidebar_visible(False)

    def on_window_command(self, window, command, args):
        if not hasattr(self, 'disable_auto_show'):
            self.disable_auto_show = False

        if command != 'toggle_side_bar':
            return
        is_going_to_be_visisble = not window.is_sidebar_visible()
        if is_going_to_be_visisble is True:
            self.disable_auto_show = True
        else:
            self.disable_auto_show = False
