# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

import wx
import subprocess
import platform
import os

class AutyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Android Auty', size=(350, 300))
        self.panel = wx.Panel(self, -1)
        #Android devices combox.
        combox_list = []
        r = execute_shell("adb devices")
        for i in range(1,len(r)-1):
            if r[i].startswith(b"*") and r[i].endswith(b"*"):
                pass
            else:
                combox_list.append(r[i].split("\t")[0])
        wx.StaticText(self.panel, -1, "Select devices:", (15, 15))
        self.devices_combobox = wx.ComboBox(self.panel, -1, r[1].split("\t")[0], (15, 35), wx.DefaultSize, combox_list, wx.CB_DROPDOWN)
        #Capture button.
        self.capture_button = wx.Button(self.panel, -1, "capture", pos=(188, 35), size=(66,25))
        self.reload_button = wx.Button(self.panel, -1, "reload", pos=(258, 35), size=(66,25))
        self.Bind(wx.EVT_BUTTON, self.captureClick, self.capture_button)
        self.Bind(wx.EVT_BUTTON, self.reloadClick, self.reload_button)
        self.capture_button.SetDefault()
        self.reload_button.SetDefault()
    def captureClick(self, event):
        capture_android(self.devices_combobox.GetValue())
        if("Windows" in platform.platform()):
            os.startfile("d:\\screenshot.png")
    def reloadClick(self, event):
        self.devices_combobox.Clear()
        k = execute_shell("adb devices")
        for i in range(1,len(k)-1):
            self.devices_combobox.Append(k[i].split("\t")[0])
        self.devices_combobox.SetValue(k[1].split("\t")[0])

def execute_shell(shell):
    p = subprocess.Popen(shell,shell=True,stdout=subprocess.PIPE)
    out = p.stdout.readlines()
    return out

def capture_android(device_id):
    sh1 = "adb -s "+device_id+" shell /system/bin/screencap -p /sdcard/screenshot.png"
    sh2 = "adb -s "+device_id+" pull /sdcard/screenshot.png d:/screenshot.png"
    execute_shell(sh1)
    execute_shell(sh2)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    AutyFrame().Show()
    app.MainLoop()