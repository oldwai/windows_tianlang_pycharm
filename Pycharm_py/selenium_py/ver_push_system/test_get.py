#coding:utf-8
'''
@author:oldwai
'''


import Ver_push_sys_BasePage
from LoginPage import Ver_push_LoginPage

#打开发布界面
login_page=Ver_push_LoginPage()
#发布版本的URL
login_page.version_release_url()
#Enter Username  输入用户名
login_page.set_username("457815031@qq.com")

#Enter password 输入密码
login_page.set_password()

#Enter indentify_code 输入验证码
login_page.set_identify_code()
login_page.wait(2)
login_page.click_login_button()

