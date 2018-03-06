#coding:utf-8
'''
@author:oldwai
'''

# encoding=utf-8
import time
import subprocess
from uiautomation import *


def demo():
    subprocess.Popen("notepad")            # 打开记事本
    window = WindowControl(ClassName="Notepad", SubName=u"记事本")    # 在桌面找到记事本

    # EditControl 编辑框组件
    edit = EditControl(searchFromControl=window)     # 找到输入框
    edit.DoubleClick()
    edit.SetValue(u'hi你好')

    # 用Win32API往记事本中写入内容
    Win32API.SendKeys(u'{Ctrl}{End}{Enter}下面开始演示{! 4}{ENTER}', 0.2)
    Win32API.SendKeys(u'0123456789{ENTER}')
    Win32API.SendKeys(u'ABCDEFGHIJKLMNOPQRSTUVWXYZ{ENTER}')
    Win32API.SendKeys(u'abcdefghijklmnopqrstuvwxyz{ENTER}')
    Win32API.SendKeys(u'`~!@#$%^&*()-_=+{ENTER}')
    Win32API.SendKeys(u'[]{{}{}}\\|;:\'\",<.>/?{ENTER}{CTRL}a')
    time.sleep(1)

    # MenuItemControl菜单组件
    menuItemFormat = MenuItemControl(searchFromControl=window, Name=u'格式(O)')
    menuItemFont = MenuItemControl(searchFromControl=window, Name=u'字体(F)...')
    windowFont = WindowControl(searchFromControl=window, Name=u'字体')

    # ComBoxControl下拉框组件
    comboScript = ComboBoxControl(searchFromControl=windowFont, AutomationId='1140')

    # ButtonControl按钮组件
    buttonOK = ButtonControl(searchFromControl=windowFont, Name=u'确定')
    menuItemFormat.Click()
    menuItemFont.Click()
    comboScript.Select(u'中文 GB2312')
    buttonOK.Click()
    time.sleep(1)
    window.Close()
    time.sleep(1)
    buttonNotSave = ButtonControl(searchFromControl=window, SubName=u'不保存')
    buttonNotSave.Click()

if __name__ == '__main__':
    demo()

