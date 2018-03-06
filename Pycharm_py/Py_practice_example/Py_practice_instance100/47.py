#coding:utf-8
'''
@author:oldwai
'''


def exchange(a,b):
     a,b=b,a
     return a,b

a=raw_input("请输入数字a："+"-"*20)
b=raw_input("请输入数字b："+"-"*20)

print exchange(a,b)

