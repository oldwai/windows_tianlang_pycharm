# coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver
import time

url = "http://www.baidu.com"
driver = webdriver.Chrome()
driver.get(url)

print "浏览器最大化"
driver.maximize_window()
time.sleep(2)

#点击新闻按钮
driver.find_element_by_link_text(u'新闻').click()
time.sleep(2)

#点击回退键
driver.back()
#前进到新闻页
driver.forward()
time.sleep(2)
#刷新一下
driver.refresh()



#设置浏览器的宽和高（分辨率）
#driver.set_window_size(800,600)

time.sleep(2)
