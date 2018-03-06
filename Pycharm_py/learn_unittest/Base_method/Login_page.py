#coding:utf-8
#author:oldwai
#email:frankandrew@163.com

import  unittest
from selenium import webdriver
#from base_page import Base_page
import base_page,time
from All_elements import Login_success_page_element

class Mail_163_login(unittest.TestCase):
    def setUp(self):
        pass
        # driver=webdriver.Chrome()
        # self.driver=driver
        # driver.get("http://mail.163.com/")

    def tearDown(self):
        # self.driver.quit()
        pass


    def test_case1(self):
        """正确的用户名和密码，登录成功"""
        test1=base_page.Base_page()
        test1.login_163_mail("frankandrew","0526oldwai")
        self.assertEqual(base_page.Base_page.islogin_success(),0)






if __name__ == '__main__':
    unittest.main()