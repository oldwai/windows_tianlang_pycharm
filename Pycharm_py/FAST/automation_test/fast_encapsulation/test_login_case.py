#coding:utf-8
'''
@author:oldwai
'''

import sys
import HTMLTestRunner
import unittest
from FAST.automation_test.fast_encapsulation.base import operation
from FAST.automation_test.fast_encapsulation.base import elements



class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        operation.PublicMethod.start_process_fast()

    @classmethod
    def tearDown(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case1(self):
        """验证正确用户名，错误密码"""
        operation.login_isli_fast('caolh', '11111')
        prompt=elements.LoginWindow.account_error_location.Name
        self.assertEqual(prompt,'用户名或密码错误！',msg='登录失败，用户名或密码错误了')

    def test_case2(self):
        """正确用户名,密码为空"""
        operation.login_isli_fast('caolh','')
        prompt=elements.LoginWindow.account_error_location.Name
        self.assertEqual(prompt, '请输入密码！',msg='未输入密码')

    def test_case3(self):
        """用户名不存在，密码正确"""
        operation.login_isli_fast('asdaszxcasdvzx', '123456')
        prompt=elements.LoginWindow.account_error_location.Name
        self.assertEqual(prompt,'用户名或密码错误！',msg='用户名密码错误')

    def test_case4(self):
        """用户名不存在，密码为空"""
        operation.login_isli_fast('caolh', '')
        prompt=elements.LoginWindow.account_error_location.Name
        self.assertEqual(prompt,'请输入密码！',msg='用户名密码错误')

    def test_case5(self):
        """用户名为空，密码正确"""
        operation.login_isli_fast('', '123456')
        prompt=elements.LoginWindow.account_error_location.Name
        self.assertEqual(prompt,'请输入用户名！',msg='用户名密码错误')

    def test_case6(self):
        """用户名、密码均为空"""
        operation.login_isli_fast('', '')
        prompt=elements.LoginWindow.account_error_location.Name
        self.assertEqual(prompt,'请输入用户名！',msg='用户名密码错误')

    def test_case7(self):
        """验证正确的账号密码登录"""
        operation.login_isli_fast('caolh','123456')
        sysman_is_exist=elements.LoginSuccessWindow.user_message.Exists(maxSearchSeconds=3)
        self.assertTrue(sysman_is_exist,msg='未找到用户信息窗口，没有登录成功')
        operation.logout()
'''
    # def testCase8(self):
    #     """验证自动登录"""
    #     if elements.LoginWindow.remember_passwd.AccessibleCurrentState() == 1048576:
    #         elements.LoginWindow.remember_passwd.Click()
    #     operation.login_isli_fast('caolh','123456')
    #     operation.PublicMethod.kill_process_fast()
    #     operation.PublicMethod.wait_for_disappear(elements.LoginSuccessWindow.root_window, 5)
    #     operation.PublicMethod.start_process_fast()
    #     sysman_is_exist=elements.LoginSuccessWindow.user_message.Exists(maxSearchSeconds=3)
    #     self.assertTrue(sysman_is_exist,msg='未找到用户信息窗口，没有登录成功')
    #     # 数据状态还原,还原为未勾选自动登录
    #     #action.logout_if_success(self)  # 登录成功则退出登录
    #     operation.logout()
    #     operation.PublicMethod.wait_for_exist(elements.LoginWindow.auto_login, 5)
    #     elements.LoginWindow.auto_login.Click()
    #     elements.LoginWindow.login_button.Click()
    #     operation.logout()
    #
    # def testCase9(self):
    #     """验证记住密码登录"""
    #
    #     if elements.LoginWindow.auto_login.AccessibleCurrentState() == 1048576:
    #         elements.LoginWindow.auto_login.Click()
    #
    #     operation.login_isli_fast('caolh','123456')
    #     operation.PublicMethod.kill_process_fast()
    #     operation.PublicMethod.start_process_fast()
    #     elements.LoginWindow.login_button.Click()
    #     sysman_is_exist=elements.LoginSuccessWindow.user_message.Exists(maxSearchSeconds=3)
    #     self.assertTrue(sysman_is_exist,msg='未找到用户信息窗口，没有登录成功')
        '''


if __name__ == "__main__":
    #unittest.main()
    testunit1 = unittest.TestSuite()
    testunit1.addTest(LoginTest("test_case1"))
    testunit1.addTest(LoginTest("test_case2"))

    #result_report = HTMLTestRunner.HTMLTestRunner


