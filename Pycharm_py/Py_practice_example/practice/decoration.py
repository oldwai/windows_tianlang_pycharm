# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

from functools import wraps

def a_new_decorator(func):
    @wraps(func)
    def wrapTheFuction():
        print ("Start")
        print ("*"*20)
        func()
        print ("*"*20)
        print ("END!!!")
    return wrapTheFuction

@a_new_decorator
def a_test():
    print ("I'm testing!!!")


print (a_test.__name__)

