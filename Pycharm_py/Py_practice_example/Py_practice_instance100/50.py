#coding:utf-8
'''
@author:oldwai
'''

#使用 random 模块。输出一个随机数


import random

##random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
print ('用于生成一个0到1的随机符点数',random.random())

#random.uniform的函数原型为：random.uniform(a, b)，用于生成一个指定范围内的随机符点数，
# 两个参数其中一个是上限，一个是下限。
# 如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。
print ('用于生成一个指定范围内的随机符点数',random.uniform(10, 20))
print ('用于生成一个指定范围内的随机符点数',random.uniform(20, 10))

#random.randint()的函数原型为：random.randint(a, b)，
# 用于生成一个指定范围内的整数。
# 其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
print (random.randint(10,20))
print (random.uniform(20,10))
#random.randrange([start], stop[, step])，
# 从指定范围内，按指定基数递增的集合中 获取一个随机数。
print (random.randrange(0,100,2))

