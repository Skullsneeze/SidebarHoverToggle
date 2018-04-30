SidebarHoverToggle
==========================

Opens the sidebar when hovering over your gutter, and closes it when hovering anywhere else

This plugin only works in Sublime text 3 (Build 3124 >), since it uses the native `on_hover` command.

Dependencies
=====

This package depends on the [MouseEventListener](https://github.com/SublimeText/MouseEventListener) package, which is available through package control.

Installation
=====

Note that this plugin has an open pull request to be added to the Package control database. For now please follow the following manual installation instructions (using package control).

1. Open up sublime, and open the command pallette (<kbd>cmd</kbd> + <kbd>shift</kbd> + <kbd>p</kbd>).
2. In the dialog, type in "add repo" (without quotes), and select the option "Package Control: Add Repository".
3. Next, a new dialog will show up, asking you for the repo URL. Use the following URL `https://github.com/Skullsneeze/SidebarHoverToggle.git`, and press enter
4. Once added, open up the command pallette again, and type in "install", and select the option "Package Control: Install Package".
5. Wait for the repositories to be loaded, and once the new dialog shows up, type in "SidebarHoverToggle", and press enter.
6. Restart Sublime (quit the app on Mac OS (<kbd>cmd</kbd> + <kbd>q</kbd>)).


Settings
=====

You can add the following parameters to your sublime Preferences to change the behaviour of this package:

Set wether or not the sidebar is toggled with the *hover* event

`"sidebar_toggle_on_hover": true`

Set wether or not the sidebar is toggled with the *click* event. You must make 1 click to [**gutter**](Doc/gutter.jpg).

`"sidebar_toggle_on_click": true`

Set wether or not the sidebar should be automatically hidden

`"sidebar_toggle_auto_hide": true`

