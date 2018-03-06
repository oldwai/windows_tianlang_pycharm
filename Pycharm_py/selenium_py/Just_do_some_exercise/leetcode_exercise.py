#coding:utf-8
'''
@author:oldwai
'''

nums = [2, 7, 11, 15]
target = 9

def func(list,target):
    for i in nums:
        for j in nums:
            print "I+J=",i+j
            # if i+j==target:
            #     return i,j

a=func(nums,target)
print a
