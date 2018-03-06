# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import datetime
import sys
import os
import platform

import subprocess


def execute_shell(shell):
    p = subprocess.Popen(shell,shell=True,stdout=subprocess.PIPE)
    out = p.stdout.readlines()
    return out

def capture_android(device_id):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
    sdcardpath = "/sdcard/adb_screen-" + now_time + ".png"
    pc_path = 'd:\\adb_screen\\adb_screen-' + now_time + '.png'
    begin_screen = "adb -s " + device_id + " shell /system/bin/screencap -p " +sdcardpath
    pull_screen = "adb -s " + device_id + " pull " + sdcardpath + " " + pc_path
    #print(begin_screen, "\n", pull_screen)
    execute_shell(begin_screen)
    execute_shell(pull_screen)
    return pc_path

if __name__ == '__main__':
    device_id = "0123456789ABCDEF"
    input('------------------------')
    pic_location = capture_android(device_id)
    if("Windows" in platform.platform()):
        os.startfile(pic_location)

