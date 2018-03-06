

# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
import time
#from TestCase_Login2 import login
#from collections import  Iterable
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
#driver.maximize_window()
base_url = "https://172.16.5.162:8443/mpr/mcrs-system/mvc/syslogin/login"
driver.get(base_url)
driver.find_element_by_id("userName").send_keys("xuxuerlai")
driver.find_element_by_id("passWord").send_keys("123456")
driver.find_element_by_id("codeCon").send_keys("1")
driver.find_element_by_id("login").click()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='menu']/div/ul/li[5]/a").click()
#//*[@id="menu"]/div/ul/li[5]/a
time.sleep(2)
driver.switch_to_frame(driver.find_element_by_xpath(".//*[@id='j_main']"))
time.sleep(2)

select=driver.find_element_by_xpath(".//*[@id='searchApplyStatus']/select")
#option_loc = ".//*[@id='searchApplyStatus']/select/option"

option_loc="//*[@id='searchApplyStatus']/select/option[1]"

options=select.find_elements_by_xpath('option')
print(options[1].text)
for i in options:
    print(i.text)

# options_list=select.find_elements_by_tag_name("option")
#
# for i in options_list:
#     values=i.get_attribute("value")
#     print values

# for i in options_list:
#     # print ("Value is: " + option.get_attribute("value"))
#     # print ("Text is:" +option.text)
# #if option_text in option.text:
#     print ("option_textoption_textoption_textValue is: " , i.text())




