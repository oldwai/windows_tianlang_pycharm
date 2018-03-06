# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import ctypes
import os



# 输出彩色字体
def print_color_font(message, font_color):
    setcolor = ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), font_color)
    print(message)
    reset_color = ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11),
                                                                 0x04 | 0x02 | 0x01)

t = os.popen('adb devices').read()  # 当adb未启动时，避免下一条卡住
devices_list = os.popen('adb devices -l | findstr "model"').readlines()
print(devices_list)
print('--------------------------------------------------------------------------------')
if devices_list:
    num = 1
    udid_list = []
    for devices in devices_list:
        udid = devices.split()[0]
        print(devices.split())
        device_name = (devices.split()[3]).split(":")[1]
        message = u'设备[%d]: %-20s\t%-20s\n' % (num, udid, device_name)
        # print_color_font(message, 0x0a)
        num += 1
        udid_list.append(udid)
    print('--------------------------------------------------------------------------------')
    print(udid_list)

