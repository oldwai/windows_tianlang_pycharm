# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import random
from tkinter import *

import tkinter.simpledialog as dl
import tkinter.messagebox as mb


mb.showinfo("猜数字游戏","欢迎您来到猜数字游戏")

number = random.randrange(1,200)
count = 0

while count < 10:
    guess = dl.askinteger("猜数字","输入你猜的数字")

    if guess == number:
        mb.showinfo("恭喜","真厉害，你猜中了,正确答案是%d!"%number)
        break

    elif guess < number:
        mb.showerror("提示",'你猜的数字太小了')
#        break
    else:
        mb.showerror("提示",'你猜的数字太大了')
#        break
    count += 1

else:
    mb.showwarning("游戏结束","正确答案是%d，你答了%d次都没有答对，真丢脸！"%(number, count))