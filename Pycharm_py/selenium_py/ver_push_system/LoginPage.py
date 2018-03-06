#coding:utf-8
'''
@author:oldwai
'''

from Ver_push_sys_BasePage import Ver_push_sys_Basepage
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Ver_push_LoginPage(Ver_push_sys_Basepage):
    #page element identifier 页面元素定位
    username=(By.NAME,"user")
    password=(By.NAME,"pwd")
    identify_code=(By.NAME,"ValidCode")
    login_button=(By.XPATH,"//button[@class='btn btn-primary btn-sm']")

    #登录版本发布
    def version_release_url(self):
        self.driver.get("http://172.16.3.112:8080/versionserver/static/index.html#/publish/login")
    #登录版本审核地址
    def version_audit_url(self):
        self.driver.get("http://172.16.3.112:8080/versionserver/static/index.html#/release/login")
    #set username 输入用户名
    def set_username(self,username):
        #username=raw_input("请输入登录的账号：")
        name=self.driver.find_element(*Ver_push_LoginPage.username)
        name.clear()
        name.send_keys(username)
    #输入密码
    def set_password(self,password="tianlang123456"):
        #password=raw_input("请输入登录账号的密码：")
        pwd=self.driver.find_element(*Ver_push_LoginPage.password)
        #清空密码输入框
        pwd.clear()
        pwd.send_keys(password)
    #输入验证码
    def set_identify_code(self):
        real_identify_code=raw_input("请输入正确的验证码：")
        code=self.driver.find_element(*Ver_push_LoginPage.identify_code)
        code.clear()
        code.send_keys(real_identify_code)
    #点击登录按钮
    def click_login_button(self):
        login_button_path=self.driver.find_element(*Ver_push_LoginPage.login_button)
        login_button_path.click()
        return self.driver
    #设置等待时间，显性等待
    def wait(self,seconds):
        '''

        :param seconds:等待时间
        :return:
        '''
        self.driver.implicitly_wait(seconds)
    #定位元素的方法封装，暂未用
    def getElement_verpush(self,by,value):
        '''
        :param by:  查找元素的方式如：id/class/css/xpath
        :param value: 文本值
        :return:    查找到的元素
        '''
        if by=="id":
            return self.driver.find_element_by_id(value)
        elif by=="name":
            return self.driver.find_element_by_name(value)
        elif by=="linktext":
            return self.driver.find_element_by_link_text(value)
        elif by=="class":
            return self.driver.find_element_by_class_name(value)
        elif by=="css":
            return self.driver.find_element_by_css_selector(value)
        elif by=="xpath":
            return self.driver.find_element_by_xpath(value)
        elif by=="tag":
            return self.driver.find_element_by_tag_name(value)
        else:
            print("请输入适合的查找元素------：")

