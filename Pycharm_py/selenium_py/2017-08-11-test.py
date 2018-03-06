#coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://new.testcooquan.ibaking.com/login.html")

username ="xxxxx"
password ="xxxxx"
driver.find_element_by_name("j_username").send_keys(username)
driver.find_element_by_name("j_password").send_keys(password)
driver.find_element_by_tag_name("button").click()

driver.getW