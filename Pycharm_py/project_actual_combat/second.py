#coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver
from time import sleep
from selenium.common.exceptions import InvalidSelectorException

#发布中心的地址
pub_site_url= "http://172.16.3.112:8080/versionserver/static/index.html#/publish/login"
login_name="457815031@qq.com"
login_pwd="tianlang123456"

driver=webdriver.Firefox()
driver.get(pub_site_url)
#定位--输入用户名密码框
path_name_frame=driver.find_element_by_name("user")
path_passwd_frame=driver.find_element_by_name("pwd")
#定位--登录按钮框
path_login_button=driver.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']")
path_identify_code=driver.find_element_by_name("ValidCode")
path_name_frame.send_keys("111111111")

# aaaaa=path_name_frame.get_attribute("value")
# print "this is aaaa的打印：",aaaaa
#text=path_name_frame.text()
print(path_name_frame.get_attribute("value"))