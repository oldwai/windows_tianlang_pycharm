#coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver
from time import sleep

url="http://mail.163.com"
#url="http://192.168.221.129/wordpress/wp-login.php"
google_driver = webdriver.Chrome()
google_driver.get(url)

google_driver.find_element_by_id("auto-id-1500365389988").clear()
google_driver.find_element_by_id("auto-id-1500365389988").send_keys("oldwai")
google_driver.find_element_by_id("user_pass").clear()
google_driver.find_element_by_id("user_pass").send_keys("W#fH4!w%WO9orXYpJf")
sleep(2)

google_driver.find_element_by_id("wp-submit").click()






