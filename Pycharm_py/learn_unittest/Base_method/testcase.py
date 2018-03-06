#coding:utf-8
'''
@author:oldwai
'''


from selenium import webdriver
import time


#driver=webdriver.Chrome()
driver=webdriver.Firefox()
driver.get("http://mail.163.com")
driver.maximize_window()
time.sleep(1)
driver.switch_to.frame("x-URS-iframe")

time.sleep(3)
#driver.find_element_by_css_selector("m-container").click()
#username=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]")
username=driver.find_element_by_name("password")
username.clear()
username.send_keys("frankandrew")
password=driver.find_element_by_name("email")
#password=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input")
password.send_keys("0526.oldwai")
login_button=driver.find_element_by_id("dologin")
login_button.click()
