#coding:utf-8
'''
@author:oldwai
'''

import os,re
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

url = "http://172.16.7.55:9000/admin/login/?next=/admin/"
driver= webdriver.Chrome()
username="admin"
password="0526.oldwai"

#登录windows上django函数
def loing_win_django():
    driver.get(url)
    sleep(2)
    driver.find_element_by_id("id_username").clear()
    driver.find_element_by_id("id_username").send_keys(username)
    driver.find_element_by_id("id_password").clear()
    driver.find_element_by_css_selector("#id_password").send_keys(password)
    sleep(1)
    driver.find_element_by_css_selector("div.submit-row>input").click()
    sleep(1)
def run_cmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text





loing_win_django()
driver.find_element_by_link_text("Questions").click()
sleep(2)

'''
# login_success_title = open_django.title
# login_success_url=open_django.current_url
# print "这是登录成功之后的web title地址：",login_success_title
# print "这是登录成功之后的URL：",login_success_url
# open_django.find_element_by_link_text("Questions").click()
# #点击Questions之后的url地址
# now_title=open_django.title
# now_url = open_django.current_url
# print("这是点击Questions之后的title：%s"%now_title)
# print("这是点击Questions之后的URL：%s"%now_url)
# if login_success_url==now_url:
#     print "登录成功的URL和点Questions之后的URL是一样的，说明有问题！！！"
# else:
#     print("两个地址不一样是正确的。")
'''
#open_django.find_elements_by_
#xpath定位时要加.作用是什么
#right=open_django.find_element_by_xpath('.//*[@id="searchbar"]')
search_input=driver.find_element_by_css_selector('#searchbar')
manual_input=raw_input("输入你要查询的信息：")
search_input.send_keys(manual_input)
sleep(1)
md5_check=search_input.get_attribute("value").decode("utf8")
print("md5_check打印：检测输入框是否有文字输入",type(md5_check),md5_check)
# if md5_check != None:
#     search_input.click()
# else:
#     print "搜索框没有输入查询条件，不点击search按钮"

#context_click定位到元素然后鼠标右击
#ActionChains(open_django).context_click(right).perform()
sleep(2)

'''
#move_to
add_quest=open_django.find_element_by_link_text("Add question")
add_quest.click()
sleep(1)
# #添加5个question
for i in range(1,6):
    open_django.find_element_by_css_selector("#id_question_text.vTextField").send_keys(i)
    sleep(1)
    open_django.find_element_by_css_selector(".collapse-toggle").click()
    sleep(1)
    open_django.find_element_by_id("id_pub_date_0").send_keys("2017-07-0%d"%i)
    open_django.find_element_by_id("id_pub_date_1").send_keys("17:44:4%d"%i)
    if i==5:
        open_django.find_element_by_name("_save").click()
    else:
        open_django.find_element_by_name("_addanother").click()
    sleep(2)
'''


#open_django.find_element_by_name("action").click()

#open_django.quit()
