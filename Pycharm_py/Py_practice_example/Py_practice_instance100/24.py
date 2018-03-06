#coding:utf-8
'''
@author:oldwai
'''

# -*- coding: UTF-8 -*-

#求2/1  3/2 5/3 8/5数列的第20个数

s =0
a,b=1.0,2.0

def calc(a,b,s):
    n =int(input("你要计算第几个数字？请输入："))
    for i in range(1,n+1):
        s =b/a
        a,b=b,a+b
    return s

