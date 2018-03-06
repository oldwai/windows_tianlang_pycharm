# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import copy
import os

import requests


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)
    __repr__ = __str__

# s = Student('Bob', 'male', 88)
# print(s)
# dic = {"ad":1,"ap":2}
#
# dict1 = {'user': 'vickey', 'num': [1, 2, 3],'age':{'a':'1','b':'2'}}
# dict2 = dict1                   # 对原始数据的任何操作都会影响该复制
# # 先进行数据的浅复制和深复制操作
# dict3 = dict1.copy()            # 浅复制: 一级为引用对象，二级为拷贝；原始数据的二级目录改变了，浅复制的数据的二级目录也会改变，但一级目录不变
# dict4 = copy.deepcopy(dict1)    # 深复制：深拷贝父对象（一级目录），子对象（二级目录）是引用，非拷贝；简单地说就是与最原始的的数据时完全一致的
# print(dict1)
# print(dict2)
# print(dict3)
# print(dict4)
#
# # 修改 data 数据
# dict1['user'] = 'root'
# dict1['num'].remove(3)
# dict1['num'].append(6)
# dict1['age']['a'] = '111'
# print("---------------------------")
# print(dict1)
# print(dict2)
# print(dict3)
# print(dict4)


# 字典数据类型的copy函数,当简单的值替换的时候，原始字典和复制过来的字典之间互不影响
#print("#字典数据类型的copy函数,当简单的值替换的时候，原始字典和复制过来的字典之间互不影响")

s = requests.Session()
headers = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.7.1 Chrome/49.0.2623.111 Safari/537.36",
    "token": "eyJhbGciOiJIUzUxMiJ9.eyJhdWQiOiIxNzIuMTYuNy41NSIsInRpY2tldCI6IjNBMkFCODNBLURGNkEtNEY3OS05MTVBLTdFOTg1NEY3MzVCNyIsInVuaWZpY2F0aW9uSWQiOjE1MTcyNzk3Nzc4MjQzNzM4LCJicmFuZElkIjoiMDAwMDAwMDIiLCJpc3MiOiI2NUNGNkQ0NkIzRjQ0RTE0QUFDRDM1REQ2NTIyNUQwNiIsInJlcXVlc3RJcCI6IjE3Mi4xNi43LjU1IiwiZXhwIjoxNTE3NDcwMzgyLCJkZXZpY2VJZCI6IjAwMDAwMDAyZWFlZjYzM2QwMGQyMTFlMzk1ZTA5YThjZWUwNzU0OTIiLCJpYXQiOjE1MTc0Njg1ODIsImp0aSI6IjFiZmFlMjZkMmI3MTQ4NjE5YTYxMjhlYjNiYWRhNWQzIn0.gJTZ6eD5ZDTPMWjk1ba2Bf30nwXJqshRY2VvzqzVWM_Vl2qGqYwR5jIwX8_enhgbC57459wFxTCWMNnqQefQ6A"
}
url = "http://172.16.3.45:11999/pms/v1/shop/messages/1402"
url2 = "http://172.16.3.45:11999/pcs/v1/buycar/add"
for i in range(1,6000):
    word = "自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试自动化测试"
    content = str(i)+word
    json = {"content":content,"customerName":"xiguanoldwai@163.com","customerId":"15172797778243738"}
    r = s.post(url, headers=headers, json=json, verify=False)
    print(r.status_code)
    print(i)