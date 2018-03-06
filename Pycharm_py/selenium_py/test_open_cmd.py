#coding:utf-8
'''
@author:oldwai
'''

#用于测试获取cmd输入的信息
from selenium import webdriver
from time import sleep


def account_login(url,push_login_name,push_login_pwd):
    global driver
    driver.get(url)
    sleep(2)
    #定位--输入用户名密码框
    path_name_frame=driver.find_element_by_name("user")
    path_passwd_frame=driver.find_element_by_name("pwd")
    #定位--登录按钮框
    path_login_button=driver.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']")
    path_identify_code=driver.find_element_by_name("ValidCode")
    path_name_frame.clear()
    path_name_frame.send_keys(push_login_name)
    path_passwd_frame.clear()
    path_passwd_frame.send_keys(push_login_pwd)
    identify_code=raw_input("请输入正确的验证码：")
    sleep(5)
    path_identify_code.send_keys(identify_code)
    login_url=driver.current_url
    path_login_button.click()
    sleep(1)
    login_success_url=driver.current_url
    return login_url,login_success_url

def verify_login_success(url_list):
    if url_list[0]==url_list[1]:
        print("登录失败，请检查原因：")
    else:
        print("登录成功")

driver=webdriver.Chrome()
#版本升级地址和登录信息和升级安装包绝对路径
ver_push_url='http://172.16.3.112:8080/versionserver/static/index.html#/publish/login'
ver_release_url='http://172.16.3.112:8080/versionserver/static/index.html#/release/login'
push_login_name="457815031@qq.com"
release_login_name="caolh@mpreader.com"
push_login_pwd="tianlang123456"

# f = account_login(ver_push_url,push_login_name,push_login_pwd)
# verify_login_success(f)
driver.get(ver_push_url)
print driver.title
