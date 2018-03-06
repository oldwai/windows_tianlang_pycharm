# -*- coding:UTF-8 -*-
import Tkinter
import tkMessageBox     #对话框
import urllib,urllib2,re
from PIL import Image



window = Tkinter.Tk()  #创建窗口
window.title("Test        GUI")
window.geometry("800x200")
name=Tkinter.Label(window,text = "姓名：",font=("微软雅黑",40),fg = "red") #文本框
name.grid() #grid是一个布局方法，place和
nameent = Tkinter.Entry(window,font =("微软雅黑",40)) #单行输入框，多行为
nameent.grid(row=0,column=1) #设置位置
button= Tkinter.Button(window,text ="一键设置签名",font =("微软雅黑",10),width="15",height="1")
button.grid(row=1,column=1) #设置button位置

window.mainloop() #运行窗口

