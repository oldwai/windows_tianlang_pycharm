
__author__="AAAAAAAAAAAA"
import sys,os
import win32gui
import win32com
import win32api
from PIL import ImageGrab
import pyHook,pythoncom
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

def onMouseEvent(event):
    print ("Position:",event.Position)


currnt_py_directory=os.getcwd()
print (currnt_py_directory)
os.startfile("D:\\MPR Install\\FAST\\FAST.exe")

'''
time.sleep(3)
m = PyMouse()
k = PyKeyboard()
x_dim, y_dim = m.screen_size()

hm = pyHook.HookManager()
hm.KeyDown = onMouseEvent
hm.HookMouse()
'''
"""
m.click(x_dim/2, y_dim/2, 1)
k.tap_key(k.tab_key)
k.tap_key(k.tab_key)
k.type_string('123456')
"""