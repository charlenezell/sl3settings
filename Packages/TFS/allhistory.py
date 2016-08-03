# -*-coding:utf8-*-
import sublime
import sublime_plugin
import os,sys,subprocess
import tfscommon.func as tfsfunc
globals()['TFSSettings']=sublime.load_settings('TFS.sublime-settings')
working_dir=TFSSettings.get('projectRoot', None)
TFRoot=TFSSettings.get('TFRoot', None)
userName=TFSSettings.get('userName', None)

def checkInconfirmDone(msg):
	args=["tf","history","*","/recursive","/format:detailed","/v:"+msg]
	print ("start;waiting...")
	stds=tfsfunc._execute_command(args,working_dir)
	output = sublime.active_window().new_file()
	# output2 = sublime.active_window().new_file()
	output3 = sublime.active_window().new_file()
	edit = output.begin_edit()
	# edit2 = output2.begin_edit()
	edit3 = output3.begin_edit()
	#源数据
	output.insert(edit,0, stds[0])
	# 去重数据
	# output2.insert(edit2,0, tfsfunc.makecontent(stds[0])[1])
	output3.insert(edit3,0, tfsfunc.makecontent(stds[0])[0])
	print ("end~~")

def checkInconfirmCancel():
	return False

def checkInconfirmChange(msg):
	return True

class AllhistoryCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Time Period",tfsfunc.recentTimestr(10),checkInconfirmDone,checkInconfirmChange,checkInconfirmCancel);
