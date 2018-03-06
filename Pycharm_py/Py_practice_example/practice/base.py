# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *   # 导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
# import importlib
# # 下面这三行代码是为了避免中文乱码问题
# import sys
# importlib.reload(sys)
# sys.setdefaultencoding('utf-8')

class BasePage(object):
    """
    基于原生的selenium框架做了二次封装.
    """
    def __init__(self):
        """
        启动浏览器参数化，默认启动firefox.
        """
        self.driver = webdriver.Firefox()
        # self.driver = driver

    def open(self, url, t='', timeout=10):
        '''
        使用get打开url后，最大化窗口，判断title符合预期
        '''
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(t))
        except TimeoutException:
            print("open %s title error" % url)
        except Exception as msg:
            print("Error:%s" % msg)

    def find_element(self, locator, timeout=10):
        '''定位元素，参数locator是元组类型'''
        element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        '''定位一组元素'''
        elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator):
        '''点击操作'''
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text, is_clear=True):
        '''
        发送文本，清空后输入
        Usage:
        locator = ("id","xxx")
        driver.send_keys(locator, text)
        '''
        element = self.find_element(locator)
        if is_clear:
            element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text, timeout=10):
        '''
        判断文本在元素里,没定位到元素返回False，定位到返回判断结果布尔值
        result = driver.text_in_element(locator, text)
        '''
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            print ("元素没定位到："+str(locator))
            return False
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        '''
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(locator, text)
        '''
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            print ("value为空，或元素没定位到："+str(locator))
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''判断title完全等于  True/False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''判断title包含    True/False'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def close(self):
        self.driver.close()

if __name__ == '__main__':
    # driver = webdriver.Firefox()
    RCS_URL = "https://172.16.5.126:9443/#/systemStart"
    test = BasePage()
    test.open(RCS_URL)
    test.find_element((""))




