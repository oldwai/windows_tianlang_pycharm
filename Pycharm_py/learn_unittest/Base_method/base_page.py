#coding:utf-8
#author:oldwai
#email:frankandrew@163.com

from selenium import webdriver
import time
from All_elements import Login_page_element
import unittest

class Base_page(unittest.TestCase):

    '''注释掉定位元素的方法
    def for_find_element(self,selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == "i" or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element



    def send_keys_func(self,selector,text):
        #定义发送值到输入框
        element_location=self.for_find_element(selector)
        element_location.clear()
        element_location.send_keys(text)


    def login_163mail(self,account,password):
        #from Base_page import for_find_element
        self.account=account
        self.password=password
        login_page=Login_page_element()
        login_url=login_page.url
        self.driver.get(login_url)
        A=Base_page()
        time.sleep(3)
        input_user=A.for_find_element(login_page.username)
        input_user.send_keys(self.account)
        time.sleep(0.5)
        input_pwd=A.for_find_element(login_page.password)
        input_pwd.send_keys(self.password)
        time.sleep(0.5)
        A.for_find_element(login_page.login_button).click()


def login(account='username',password='password'):
    test_login=Base_page()
    test_login.login_163mail(account,password)

'''
    def open_mail_website(self,login_url):
        #driver=webdriver.Firefox()
        driver=webdriver.Chrome()
        self.driver=driver
        self.driver.get(login_url)
        time.sleep(2)
        self.driver.switch_to.frame("x-URS-iframe")

    def get_element(self,selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        print type(selector_by),selector_by,type(selector_value),selector_value
        time.sleep(3)
        if selector_by == "i" or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element


    def input_info(self,selector,text):
        """
        Operation input box.
        Usage:
        driver.type("i,el","selenium")
        """
        element_location=self.get_element(selector)
        time.sleep(0.5)
        element_location.clear()
        element_location.send_keys(text)

    def click_button(self,selector):
        element_location=self.get_element(selector)
        time.sleep(0.5)
        element_location.click()

    def login(self,username,password):
        login_info=Login_page_element()
        self.open_mail_website(login_info.login_url)
        self.input_info(login_info.username,username)
        self.input_info(login_info.password,password)
        self.click_button(login_info.login_button)
        time.sleep(3)
        current_url=self.driver.current_url
        return current_url

    def islogin_success(self):
        #返回1为失败，返回0为成功
        time.sleep(3)
        return self.driver.current_url==Login_page_element.login_url

    #def url_




