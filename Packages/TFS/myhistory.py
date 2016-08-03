# -*-coding:utf8-*-
import sublime
import sublime_plugin
import os,sys,subprocess
import tfscommon.func as tfsfunc

def checkInconfirmDone(msg):
    globals()['TFSSettings']=sublime.load_settings('TFS.sublime-settings')
    working_dir=TFSSettings.get('projectRoot', None)
    TFRoot=TFSSettings.get('TFRoot', None)
    userName=TFSSettings.get('userName', None)
    # print(userName,msg)
    args=["tf","history","*","/recursive","/format:detailed","/user:"+userName,"/v:"+msg]
    # print ("start;waiting...")
    stds=tfsfunc._execute_command(args,working_dir)
    # output = sublime.active_window().new_file()
    # output2 = sublime.active_window().new_file()
    output3 = sublime.active_window().new_file()
    # output.run_command("insert", {"characters": stds[0]})
    output3.run_command("insert", {"characters": tfsfunc.makecontent(stds[0])[0]})
    # print(stds)
# >>> a=sublime.active_window().new_file()
# >>> ed=a.begin_edit()
# >>> a.insert(ed,0,view.substr(sublime.Region(0,sublime.active_window().active_view().size())))
    # print ("end~~")

def checkInconfirmCancel():
    return False

def checkInconfirmChange(msg):
    return True

class MyhistoryCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Time Period",tfsfunc.recentTimestr(10),checkInconfirmDone,checkInconfirmChange,checkInconfirmCancel);
