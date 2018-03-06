# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import random

import xlrd

# xl = xlrd.open_workbook('xlrd_practice.xlsx')
# table = xl.sheet_names()


def read_exrcl(table, row, col):
    vlaue = table.cell_value(row, col)
    type = table.cell_type(row, col)
    if type == 0:
        vlaue = "''"
    elif type == 1:
        vlaue = vlaue
    elif type == 2 and vlaue % 1 == 0:
        vlaue = int(vlaue)
    elif type == 3:
        vlaue = xlrd.xldate_as_datetime(vlaue, 0)
    elif type == 4:
        vlaue = True if vlaue == 1 else False
    return vlaue

list1 = range(0, 9)
list2 = range(20,30)
tuple1 = ('a','b','c','d','e',)

random_num =''.join([str(i) for i in random.sample(tuple1, 5)])
print(random_num)
fruit_dict = {'apple':1, 'banana':2, 'orange':3}
print(tuple(fruit_dict))