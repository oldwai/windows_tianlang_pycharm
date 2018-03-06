# -*- coding:utf-8 -*-
"""
@author:oldwai
"""
# email: frankandrew@163.com


class A(object):
    def show(self):
        print ('base show')

class B(A):
    def show(self):
        print ('derived show')

obj = B()
obj.show()