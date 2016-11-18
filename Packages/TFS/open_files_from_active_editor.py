import sublime
import sublime_plugin
import os,sys,re
import tfscommon.func as tfsfunc
globals()['TFSSettings']=sublime.load_settings('TFS.sublime-settings')
working_dir=TFSSettings.get('projectRoot', None)
TFRoot=TFSSettings.get('TFRoot', None)
class OpenFilesFromActiveEditorCommand(sublime_plugin.WindowCommand):
    def get_lines(self):
        view = self.window.active_view()
        selection = ""
        for region in view.sel():
            # If no selection, use the entire file as the selection
            if region.empty():
                selection = sublime.Region(0, view.size())
            else:
                selection = region
        return view.lines(selection)
    def get_content(self):
        view = self.window.active_view()
        selection = ""
        for region in view.sel():
            # If no selection, use the entire file as the selection
            if region.empty():
                selection = sublime.Region(0, view.size())
            else:
                selection = region
        return view.substr(selection)

    def run(self):
        view = self.window.active_view()
        for line in self.get_lines():
            a=r'\$\/projectA'
            b=re.sub(a,working_dir,view.substr(line))
            self.window.open_file(b)
    def is_enabled(self):
        return True
