import sublime
import sublime_plugin
import os,sys
import tfscommon.func as tfsfunc
globals()['TFSSettings']=sublime.load_settings('TFS.sublime-settings')
working_dir=TFSSettings.get('projectRoot', None)
TFRoot=TFSSettings.get('TFRoot', None)
class CheckOutAllCommand(sublime_plugin.WindowCommand):
	def run(self):
		openTabs = self.window.views()
		for key in openTabs:
			cmdToRun=["TF","checkout",key.file_name()]
			stds=tfsfunc._execute_command(cmdToRun,working_dir)
			print (stds[0])
	def is_enabled(self):
		return True
