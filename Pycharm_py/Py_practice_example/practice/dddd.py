# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


# value = int(input("enter a num"))
# #print(max(min(value, 50), 10))
# a = 5 if value else 2
#print(a)
import random
from functools import reduce

import time
from selenium.webdriver import ActionChains



class A:
    def __init__(self,a):
        self.a = a

    def __a(self):
        print("my name is A.a")

    def test(self):
        print('003模块里的类A下的test函数',self.a)

class B(A):
    def __a(self):
        print("my name is B.a")

def f(x, y):
    return x + y

def func(x,y):
    return x*y


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import uiautomation

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=123&oq=fds&rsv_pq=8296ff4400022123&rsv_t=c71636MBRH8aNgdYVg%2BWAJifsRjKuBTZGWOKJhVfs4G5uDXOMThIg0pI4as&rqlang=cn&rsv_enter=1&inputT=694&rsv_sug3=10&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_sug4=6926")
# # js = 'document.getElementById("setf").target="";'
# # driver.execute_script(js)
# # driver.find_element_by_id("setf").click()
# # driver.find_element_by_link_text("百度首页").click()
# time.sleep(2)
# handles = driver.window_handles
# print(handles)
# for i in range(5):
#     uiautomation.SendKeys("{Ctrl}(t)")
#     handles = driver.window_handles
#     print("第%d标签页的句柄"%i,driver.current_window_handle)
#     print(handles)
#     driver.switch_to.window(handles[i])
#     driver.get("https://www.baidu.com")
current_handle = driver.current_window_handle
# uiautomation.SendKeys("{Ctrl}(t)")
#if driver.current_window_handle ==
# driver.get("https://www.yun.baidu.com")
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
print(driver.title)