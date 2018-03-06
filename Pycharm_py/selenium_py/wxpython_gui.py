#coding:utf-8
'''
@author:oldwai
'''

import wx
app=wx.App()
window = wx.Frame(None,title="验证码输入框",size=(410,335))
btn = wx.Button(window)
window.Show()
app.MainLoop()
