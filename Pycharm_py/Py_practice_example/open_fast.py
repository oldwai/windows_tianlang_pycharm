#coding:utf-8
'''
@author:oldwai
'''

import subprocess
import time

class PublicMethod:
    # <editor-fold desc="start_process_fast 运行FAST">
    @staticmethod
    def start_process_fast():
        subprocess.Popen("C:\\Program Files (x86)\\MPRTimes\\ISLI FAST\\ISLI FAST.exe")
    # </editor-fold>
    @staticmethod
    def kill_process_fast():
        #关闭FAST进程
        subprocess.Popen('taskkill /F /IM "ISLI FAST.exe"',stdout=subprocess.PIPE,shell=True)

for i in range(10):
    PublicMethod.start_process_fast()
time.sleep(2)
PublicMethod.kill_process_fast()

input()

if __name__ == "__main__":
    pass
    # for i in range(10):
    #     PublicMethod.start_process_fast()
    # time.sleep(2)
    # PublicMethod.kill_process_fast()