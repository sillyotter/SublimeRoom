import sublime, sublime_plugin

key = 'center_cursor_vertically'

class ToggleKeepCursorCenteredCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view;
		origVal = v.settings().get(key, False)
		v.settings().set(key, not origVal)

	def is_enabled(self):
		return True

	def is_visible(self):
		return True

	def is_checked(self):
		return self.view.settings().get(key, False)

	def description(self):
		return "Toggles keeping the cursor line centered, like in WriteRoom"


class KeepCursorCentered(sublime_plugin.EventListener):
	def on_selection_modified(self, view):
		try:
			if (view.settings().get('center_cursor_vertically', False)):
				view.show_at_center(view.sel()[0])
		except:
			pass

