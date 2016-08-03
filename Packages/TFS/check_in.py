import sublime
import sublime_plugin
import os,sys

# sys.setdefaultencoding('cp936')
# stdout = sys.stdout
# stdin = sys.stdin
# reload(sys)
# sys.stdout = stdout
# sys.stdin = stdin

globals()['TFSSettings']=sublime.load_settings('TFS.sublime-settings')
working_dir=TFSSettings.get('projectRoot', None)
TFRoot=TFSSettings.get('TFRoot', None)
def checkInconfirmDone(msg):
	fileName=sublime.active_window().active_view().file_name()
	print (msg.encode("cp936"));
	# cmdToRun=["TF","checkin",fileName,"/comment:"+msg.encode("cp936")]
	# sublime.active_window().run_command('exec',{
 #        'cmd': cmdToRun,
 #        'working_dir':TFRoot,
 #        'encoding':'cp936'
 #    });	
def checkInconfirmCancel():
	return False

def checkInconfirmChange(msg):
	return False

class CheckInCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("signInReason","",checkInconfirmDone,checkInconfirmChange,checkInconfirmCancel)
	def is_enabled(self):
		fileName=self.window.active_view().file_name()
		if os.access(fileName, os.W_OK):
			return False
		else :
			return False