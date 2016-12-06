import sublime, sublime_plugin

class SidebarToggleListener(sublime_plugin.EventListener):
    
    # listen for the hover command so we can toggle the sidebar when hovering over the gutter
    def on_hover(self, view, point, hover_zone):
        # check if the attribute exists to prevent AttributeError Exception
        if not hasattr(self, 'disable_auto_show'):
            self.disable_auto_show = False
        # if the auto show is disabled, stop executing
        if self.disable_auto_show:
            return

        if hover_zone == sublime.HOVER_GUTTER:
            # hover over gutter. open the sidebar
            view.window().set_sidebar_visible(True)
        else:
            # hide sidebar
            view.window().set_sidebar_visible(False)

    # listen for every window_command so we know if a user opened the sdiebar manually
    def on_window_command(self, window, command, args):
        # check if the attribute exists to prevent AttributeError Exception
        if not hasattr(self, 'disable_auto_show'):
            self.disable_auto_show = False
        
        # only continue if the command if toggle_side_bar
        if command != 'toggle_side_bar':
            return
        
        # the side bar is hidden, but because this function is fired
        # before the command is run, the side bar is going to be in the opposite state
        is_going_to_be_visisble = not window.is_sidebar_visible()
        
        # if this condition is true, it means that the user showed the side bar manually
        # so we disable auto hide/show
        if is_going_to_be_visisble is True:
            self.disable_auto_show = True
        else:
            self.disable_auto_show = False
