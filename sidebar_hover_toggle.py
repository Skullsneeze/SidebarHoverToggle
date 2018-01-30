import sublime, sublime_plugin

# global settings
settings = {}

def plugin_loaded():
    global settings
    settings = sublime.load_settings("Preferences.sublime-settings")

"""
Thanks to FichteFoll
See https://forum.sublimetext.com/t/hover-click-events-in-gutter/20747/6
"""
def is_coord_on_gutter(view, x, y):
    """Determine if x and y coordinates are over the gutter.

    Because this is inapplicable for empty lines,
    returns `None` to let the caller decide on what do to.
    """
    original_pt = view.window_to_text((x, y))
    if view.rowcol(original_pt)[1] != 0:
        return False

    # If the line is empty,
    # we will always get the same textpos
    # regardless of x coordinate.
    # Return `None` in this case and let the caller decide.
    if view.line(original_pt).empty():
        return None

    # ST will put the caret behind the first character
    # if we click on the second half of the char.
    # Use view.em_width() / 2 to emulate this.
    adjusted_pt = view.window_to_text((x + view.em_width() / 2, y))
    if adjusted_pt != original_pt:
        return False

    return True

class SidebarToggleListener(sublime_plugin.EventListener):
    # listen for the hover command so we can toggle the sidebar when hovering over the gutter
    def on_hover(self, view, point, hover_zone):

        # only toggle on hover if set by user
        if not settings.get('sidebar_toggle_on_hover', False):
            return;

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
            # hide sidebar if auto hide is enabled
            if not settings.get('sidebar_toggle_auto_hide', False):
                return;
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

    # use the MouseEventListener package to target mouse events for toggling the sidebar
    def on_pre_mouse_down(self, click):
        # only toggle on click if set by user
        if not settings.get('sidebar_toggle_on_click', True):
            return;

        # store mouse click location
        x_location = click['event']['x'];
        y_location = click['event']['y'];

        # get the (estimated) gutter width
        min_gutter_width = 46;
        gutter_margin = settings.get("margin", 4);
        gutter_width = min_gutter_width + gutter_margin;

        # store active window
        active_window = sublime.active_window();
        active_view = active_window.active_view()
        gutter_click = is_coord_on_gutter(active_view, x_location, y_location);

        # toggle sidebar to open state only when gutter click is set to none
        if gutter_click == None and x_location <= gutter_width:
            gutter_click = True

        # check if we clicked the gutter
        if gutter_click:
            # hide sidebar when visible
            if active_window.is_sidebar_visible():
                active_window.set_sidebar_visible(False)
            # show sidebar when not visible
            else:
                active_window.set_sidebar_visible(True)
