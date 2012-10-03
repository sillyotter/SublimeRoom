import sublime, sublime_plugin
import SublimeRoomShared

class ToggleKeepCursorCenteredCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view;
		origVal = v.settings().get(SublimeRoomShared.key, False)
		v.settings().set(SublimeRoomShared.key, not origVal)

	def is_enabled(self):
		return True

	def is_visible(self):
		return True

	def is_checked(self):
		return self.view.settings().get(SublimeRoomShared.key, False)

	def description(self):
		return "Toggles keeping the cursor line centered, like in WriteRoom"
