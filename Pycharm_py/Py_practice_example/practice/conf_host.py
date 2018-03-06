# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


#coding:utf-8
import wx
import os

class Frame(wx.Frame):
    def __init__(self):#工具的显示和相关处理
        wx.Frame.__init__(self,None,-1,'SwithHosts Example',size=(1000,600))
        panel=wx.Panel(self,-1)
        ReadButton = wx.Button(panel, label = u'打开host',pos = (225,5),size = (80,25))
        ReadButton.Bind(wx.EVT_BUTTON, self.Read)#给button添加事件
        saveButton = wx.Button(panel, label = u'保存host',pos = (315,5),size = (80,25))
        saveButton.Bind(wx.EVT_BUTTON,self.Save)#给button添加事件

        self.filename = 'C:\Windows\System32\drivers\etc\hosts'#host文件路径
        self.contents = wx.TextCtrl(panel, pos = (5,35),size = (500,250), style = wx.TE_MULTILINE)

        hbox=wx.BoxSizer()
        hbox.Add(ReadButton,proportion=0,flag=wx.RIGHT|wx.HORIZONTAL)
        hbox.Add(saveButton,proportion=0,flag=wx.RIGHT|wx.HORIZONTAL)
        hbox.Add(self.contents,proportion=1,flag=wx.EXPAND|wx.ALL)
        panel.SetSizer(hbox)

    def Read(self,event):#读取host文件并显示在工具中
        file = open(self.filename)
        all_the_text=file.read()
        self.contents.SetValue(all_the_text)

    def Save(self,event):#读取工具中的输入内容后写入到host中
        value=self.contents.GetValue()
        file = open(self.filename,'w')
        file.write(value)
        file.close()

if __name__ == "__main__":
    App=wx.PySimpleApp()
    frame=Frame()
    frame.Show()
    App.MainLoop()