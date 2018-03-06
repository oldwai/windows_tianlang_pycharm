#coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Ver_push_sys_autoupgrade():
    def __init__(self,browser='chrome'):
        '''
        :param browser:浏览器对象
        :return:
        '''
        if browser=="firefox":
            driver=webdriver.Firefox()
        elif browser=="chrome":
            driver=webdriver.Chrome()
        #elif browser=="ie":
            #DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
            #driver=webdriver.Ie()
        try:
            self.driver =driver
        except Exception:
            raise NameError("没有找到该浏览器，你可以输入‘firefox’,'Chrome'选择")


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

    def max_window(self):
        '''

        :return: 最大化窗口
        '''
        self.driver.maximize_window()

    def getUrl(self,url):
        '''

        :param url:要访问的URL地址
        :return:
        '''
        self.driver.get(url)

    def login_publish_website(self):
        self.getElement_verpush()


    def wait(self,seconds):
        '''

        :param seconds:等待时间
        :return:
        '''
        self.driver.implicitly_wait(seconds)

    def close_browser(self):
        '''

        :return:  关闭窗口
        '''
        self.driver.close()

    def quit_browser(self):
        '''
        Closes the current window.
        关闭当前窗口。
        Quits the driver and closes every associated window.
        退出驱动并关闭所有关联的窗口。
        :return: 退出浏览器
        '''
        self.driver.quit()