#coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://sahitest.com/demo/linkTest.htm")

driver.find_element_by_partial_link_text("")
driver.find_element_by_link_text("linkByContent").click()

driver.find_element_by_link_text("Back").click()