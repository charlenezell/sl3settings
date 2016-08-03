import sublime
import sublime_plugin
import os,sys
import tfscommon.func as tfsfunc
globals()['TFSSettings']=sublime.load_settings('TFS.sublime-settings')
working_dir=TFSSettings.get('projectRoot', None)
TFRoot=TFSSettings.get('TFRoot', None)
class AddToTfsCommand(sublime_plugin.WindowCommand):
    def run(self):
        fileName=sublime.active_window().active_view().file_name()
        cmdToRun=["TF","add",fileName]
        stds=tfsfunc._execute_command(cmdToRun,working_dir)
        print (stds[0])
    def is_enabled(self):
        return True
