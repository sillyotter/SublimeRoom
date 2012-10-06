import sublime, sublime_plugin
import SublimeRoomShared

class KeepCursorCenteredEventListener(sublime_plugin.EventListener):
	def on_selection_modified(self, view):
		try:
			if (view.settings().get(SublimeRoomShared.key, False)):
				sel = view.sel()[0]
				if sel.a == sel.b:
					view.show_at_center(view.sel()[0])
		except:
			pass

