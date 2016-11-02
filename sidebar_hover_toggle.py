import sublime, sublime_plugin

class SidebarToggleListener(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        if hover_zone == sublime.HOVER_GUTTER:
            # hover over gutter. open the sidebar
            view.window().set_sidebar_visible(True)
        else:
            # hide sidebar
            view.window().set_sidebar_visible(False)
