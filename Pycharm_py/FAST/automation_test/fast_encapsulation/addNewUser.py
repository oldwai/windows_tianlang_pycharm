# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

import unittest
from FAST.automation_test.fast_encapsulation.base import elements
from FAST.automation_test.fast_encapsulation.base import operation

class AddNewUser(unittest.TestCase):
    def setUp(self):
        operation.PublicMethod.start_process_fast()
        operation.login_isli_fast('caolh','123456')
        operation.switch_to_sysmanage()
    def tearDown(self):
        pass

    def test_add_user_success(self):
        '''
        成功新增用户
        :return:
        '''
        operation.add_new_account('test0001','测试0001')
        error_prompt=elements.AddNewuserWindow.error_prompt.Name
        self.assertEqual(error_prompt,'',msg='成功创建一个用户')

    def testCase2(self):
        '''
        已存在的用户名，提示已存在不能创建
        :return:
        '''
        operation.add_new_account('test0001','测试0001')
        error_prompt=elements.AddNewuserWindow.error_prompt.Name
        self.assertEqual(error_prompt,'该用户名已存在！',msg='用户名已存在创建失败')
        elements.AddNewuserWindow.cancel_button.Click()
    def testCase3(self):
        '''
        已存在的用户名，提示已存在不能创建
        :return:
        '''
        operation.add_new_account('test0001','测试0001')
        error_prompt=elements.AddNewuserWindow.error_prompt.Name
        self.assertEqual(error_prompt,'该用户名已存在！',msg='用户名已存在创建失败')
        elements.AddNewuserWindow.cancel_button.Click()
    def testCase2(self):
        '''
        已存在的用户名，提示已存在不能创建
        :return:
        '''
        operation.add_new_account('test0001','测试0001')
        error_prompt=elements.AddNewuserWindow.error_prompt.Name
        self.assertEqual(error_prompt,'该用户名已存在！',msg='用户名已存在创建失败')
        elements.AddNewuserWindow.cancel_button.Click()
    def testCase2(self):
        '''
        已存在的用户名，提示已存在不能创建
        :return:
        '''
        operation.add_new_account('test0001','测试0001')
        error_prompt=elements.AddNewuserWindow.error_prompt.Name
        self.assertEqual(error_prompt,'该用户名已存在！',msg='用户名已存在创建失败')
        elements.AddNewuserWindow.cancel_button.Click()



