# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

import random
from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

mb.showinfo("猜拳游戏","欢迎您来到猜拳游戏")

while True:
    s = int(random.randint(1, 3))

    #将随机生成的数字表示为对应的字符
    if s == 1:
        ind = "石头"
    elif s == 2:
        ind = "剪刀"
    elif s == 3:
        ind = "布"
    guess_list = ['石头', "剪刀", "布"]

    #打印随机生成的结果
    print(ind)

    #调用simpldialog显示弹出框.可以获取输入框里输入的内容
    m = dl.askstring("猜拳游戏","请输入石头、剪刀、布,退出输入exit")

    #输入为空或者输入的字符不在
    if m.lower() == 'exit':
        break
    if m not in guess_list or not m:
        mb.showinfo("提示","输入错误了，请输入石头、剪刀、布")

    #如果输入条件正常，进行判断，弹出提示框显示结果
    else:
        if m == ind :
            mb.showinfo("提示","哎呀，你们都出了%s \n打平了!"% m)

        elif (m == '石头' and ind =='剪刀') or (m == '剪刀' and ind =='布') or (m == '布' and ind =='石头'):
            mb.showinfo("恭喜","真厉害，电脑出了%s,\n你出了%s ，\n你赢了！"% (ind,m))
            #break

        elif (m == '石头' and ind =='布') or (m == '剪刀' and ind =='石头') or (m == '布' and ind =='剪刀'):
            mb.showinfo("恭喜","太丑了，电脑出了%s,\n你出了%s ，\n你输了！"% (ind,m))

else:
    mb.showwarning("游戏结束","退出游戏！")