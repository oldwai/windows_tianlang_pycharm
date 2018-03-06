#coding:utf-8
'''
@author:oldwai
'''

import  Tkinter
import tkMessageBox


def input_message():
    #user_input=var_input_info.get()
    print("你输入的版本号是：",var_input_info.get())
    #string=str("版本号：%s"%user_input)
    #print("刚刚你输入的版本号为：%s"%user_input)
    #tkMessageBox.showinfo(title="版本号提示信息",message=string)

window = Tkinter.Tk()  #创建窗口
window.title("输入版本信息")
window.geometry("300x100")
input_info =Tkinter.Label(window,text='版本号：')
input_info.grid(row=0)
input_info.pack()
#显示输入框
var_input_info =Tkinter.StringVar()
#var_input_info.set("111111")
entry_input_info =Tkinter.Entry(window,textvariable=var_input_info)
entry_input_info.grid(row=0,column=1)
entry_input_info.pack()
#nameent = Tkinter.Entry(window,font =("微软雅黑",20)) #单行输入框，多行为
#nameent.grid(row=0,column=1) #设置位置
b_login = Tkinter.Button(window,text='确定')#,command=input_message())
#b_login.bind("<Button-1>",input_message()).
#b_login.grid(row=1,column=1)
b_login.pack()
b_login.bind("<Button_1>",input_message())

#window.bind("Return",callback())
window.mainloop()
