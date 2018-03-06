# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

import os

pwd1 = r'12/34/56/12312211221'#/file_rd001.py'
# t = os.path.split(pwd1,3)
# print(t)
# t = os.path.dirname(pwd1)
t = pwd1.split('/',2)

print(t)

