#coding:utf-8
'''
@author:oldwai
'''


from ver_push_system import Ver_push_sys_BasePage
from ver_push_system.LoginPage import Ver_push_LoginPage
from ver_push_system.Release_Version_page import Release_Version_page

#版本发布登录类的实例化
login_page=Ver_push_LoginPage()
#打开发布界面
login_page.version_release_url()
#Enter Username  输入用户名
login_page.set_username("457815031@qq.com")
#Enter password 输入密码
login_page.set_password("tianlang123456")
#Enter indentify_code 输入验证码
login_page.set_identify_code()
login_page.wait(2)
#点击登录
driver=login_page.click_login_button()

#cur_url=login_page.driver.current_url()
login_success_url="http://172.16.3.112:8080/versionserver/static/index.html#/publish/index"

#登录成功后，进入发布版本页面
#if cur_url==login_success_url:
release_instance=Release_Version_page(driver)
release_instance.click_release_button()
release_instance.release_client()


