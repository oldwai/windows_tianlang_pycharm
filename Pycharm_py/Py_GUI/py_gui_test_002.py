# -*- coding:UTF-8 -*-
import Tkinter
import tkMessageBox     #对话框
import urllib,urllib2,re
from PIL import Image

window = Tkinter.Tk(className="你在想什么")  #创建窗口
#window.title("你在想什么")
window.geometry("1000x100")
name=Tkinter.Label(window,text = "就是觉得很迷茫，迷茫的不知道未来那么长，该怎么走",font=("微软雅黑",30),fg = "red") #文本框
name.grid() #grid是一个布局方法，place和
#nameent = Tkinter.Entry(window,font =("微软雅黑",40)) #单行输入框，多行为
#nameent.grid(row=0,column=1) #设置位置
window.mainloop()