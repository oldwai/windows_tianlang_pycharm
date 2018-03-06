#coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver
# from selenium.webdriver.remote import switch_to
# from selenium.webdriver.common import alert
# import unittest
import time,os
from selenium.common.exceptions import NoAlertPresentException
# def users_zidian():
#     users={'1':['mpr_nimda','123456'],['mpr','123456']:'1',['mpr_nimda','234567']:'1'}
#     l=len(users)
#     print('成功读取%s个用户名和密码库！'%l)
#     return users
users={'1':{'mpr_nimda':'123456'}}
i=0
for ver_code,login_info in users.items():
    #_zidian().items():  使用for循环和字典的items（）方法遍历字典#
    i=i+1  #用来记录输入用户名和密码的次数
    print(login_info.keys(),login_info.values(),ver_code[i-1])
    driver=webdriver.Chrome()
    driver.get('https://172.16.5.162:8443/mpr/mcrs-system/mvc/syslogin/login')
    driver.find_element_by_id("userName").clear()
    driver.find_element_by_id("userName").send_keys(login_info.keys())#传递用例user参数#
    time.sleep(3)
    driver.find_element_by_id("passWord").clear()
    driver.find_element_by_id("passWord").send_keys(login_info.values())#传递用例pwd参数#
    time.sleep(3)
    driver.find_element_by_id("codeCon").clear()
    driver.find_element_by_id("codeCon").send_keys(ver_code[i-1])
    time.sleep(5)
    driver.find_elements_by_class_name("login-btn").click()
