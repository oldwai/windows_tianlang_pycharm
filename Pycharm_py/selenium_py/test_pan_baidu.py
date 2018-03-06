#coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver
from time import sleep

driver =webdriver.Firefox()
sleep(5)
driver.get("https://pan.baidu.com")
sleep(5)
driver.find_element_by_link_text("帐号密码登录").click()
# driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="myhtml"]/body/iframe'))
# nowhandle=driver.current_window_handle
# driver.switch_to.window(nowhandle)
# driver.find_element_by_xpath("//*[@id='login-middle']/div/div[6]/div[2]/a").click()

