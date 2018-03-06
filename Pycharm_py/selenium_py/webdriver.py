# -*- coding:UTF-8 -*-
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://www.baidu.com")
browser.find_element_by_id("kw").send_keys("Eric_guodongliang")
browser.find_element_by_id("su").submit()
