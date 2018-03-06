#coding:utf-8
'''
@author:oldwai
'''


from selenium import webdriver

class Ver_push_sys_Basepage(object):
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



