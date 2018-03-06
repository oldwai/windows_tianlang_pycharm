# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import subprocess
from time import sleep
import  uiautomation

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from FAST.automation_test.fast_encapsulation.base.rcs_elements import HomePage

class BaseMethod:
    RCS_URL = "https://172.16.5.126:9443/#/systemStart"
    def __init__(self):
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
    #弹窗时选择打开或者关闭FAST
    def web_open_fast(self,open=None):
        """
        弹窗非Alert窗口时，使用键盘控制点击弹窗的按钮
        :param open:
        :return:
        """
        root_window = uiautomation.WindowControl(searchDepth=1,Name ="RootContentServer")
        click_open_alert = uiautomation.ButtonControl(Name ="打开 MPRTimes.ISLIFAST")
        click_close_fast_alert = uiautomation.ButtonControl(Name ="不要打开")
        remeber_choose = uiautomation.CheckBoxControl(Name ="记住我对MPRTimes.ISLIFAST链接的选择")
        if open:
            click_open_alert.Click()
        else:
            click_close_fast_alert.Click()

    def open_browser(self,url, t='',timeout = 10):
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver,timeout,1).until(EC.title_contains(t))
        except TimeoutException:
            print("open %s title error" % url)
        except Exception as msg:
            print("Error:%s" % msg)

    def kill_process_fast(self):
        #关闭FAST进程
        subprocess.Popen('taskkill /F /IM "ISLI FAST.exe"',stdout=subprocess.PIPE,shell=True)
        #subprocess.Popen('taskkill /F /IM ISLIPublisher.exe', stdout=subprocess.PIPE, shell=True)

    def find_element(self,locator, timeout = 10):
        "定位元素，传递一个元祖类型，如（'id','//[@class='one']'）"
        element = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self,locator, timeout = 10):
        "定位一组元素，传递一个元祖类型，如（'id','//[@class='one']'）"
        elements = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_elements_located(locator))
        return elements

    def click(self,locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text, is_clear = True):
        element = self.find_element(locator)
        if is_clear:
            element.clear()
        element.send_keys(text)

    # def close(self):
    #     self.driver.close()


def open_newtab(self, username,password = "123456",url = None):
    import uiautomation
    num = 12
    for i in range(num):
        uiautomation.SendKeys("{Ctrl}(t)")

    handles = self.driver.window_handles
    current_handle = self.driver.current_window_handle
    k=0
    for handle in handles:
        if current_handle == handle:
            continue
        else:
            self.driver.switch_to.window(handle)
            self.login_rcs(username[k],password,url)
            #self.driver.switch_to.default_content()
            sleep(1)
            self.elements_method('xpath',HomePage.xpath_fast,'click')
            sleep(1)
            BaseMethod.web_open_fast(1)
            k+=1

if __name__ == "__main__":
    # login_info = ["num001","num002","num003","num004","num005",\
    #               "num006","num007","num008","num009","num010","num011","num012"]
    # #本根服务器的地址
    # RCS_URL = "https://172.16.5.126:9443/#/systemStart"
    #account = "admin"
    # username = "admin"
    # password = "a123456"
    #self.driver = webself.driver.Chrome()
    #self.driver.find_element_by
    driver = webdriver.Chrome()
    username = "caoleihua"
    password = "123456"
    RCS_URL = "https://172.16.3.251:9443/#/systemStart"
    login_rcs(username,password,RCS_URL)

