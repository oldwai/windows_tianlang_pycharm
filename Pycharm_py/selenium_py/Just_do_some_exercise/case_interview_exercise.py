#coding:utf-8
'''
@author:oldwai
'''

#面试题 list和dict的区别，如何遍历list和字典

#list是有序的序列，数据是可重复的；字典是无序的，不可重复，键值一一对应
#dict的占用内存稍比list大，会在1.5倍左右

list1=range(1,10)
print "打印list1的数据：",list1
dic1={"a":1,"b":2,"c":3}
print "字典dic1：",dic1

for key,value in dic1.items():
    print key,":",value


