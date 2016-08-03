import sublime
import sublime_plugin
import subprocess
globals()['TFSSettings']=sublime.load_settings('TFS.sublime-settings')
working_dir=TFSSettings.get('projectRoot', None)
TFRoot=TFSSettings.get('TFRoot', None)
class TfsOneCommand(sublime_plugin.WindowCommand):
	def run(self,itype,iarg):
		print (itype,iarg)
		cmdtoRun=["TF",itype,self.window.active_view().file_name(),iarg]
		subprocess.Popen(cmdtoRun)
	def is_enabled(self):
		return True
