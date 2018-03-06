#coding:utf-8
'''
@author:oldwai
'''

import subprocess
import uiautomation
import elements
# from FAST.automation_test.fast_encapsulation.base import elements
import time
from importlib import reload

class PublicMethod:

    # <editor-fold desc="start_process_fast 运行FAST">
    @staticmethod
    def start_process_fast():
        subprocess.Popen("C:\\Program Files (x86)\\MPRTimes\\ISLI FAST\\ISLI FAST.exe")
        root_window = uiautomation.PaneControl(searchDepth=1, ClassName='Qt5QWindow')
        # uiautomation.WaitForExist(root_window, 1)
        root_window.ShowNormal()  # 激活显示
        root_window.SetWindowTopmost(True)  # 置顶显示
    # </editor-fold>
    @staticmethod
    def kill_process_fast():
        #关闭FAST进程
        subprocess.Popen('taskkill /F /IM "ISLI FAST.exe"',stdout=subprocess.PIPE,shell=True)
        #subprocess.Popen('taskkill /F /IM ISLIPublisher.exe', stdout=subprocess.PIPE, shell=True)
        reload(elements)

    @staticmethod
    def input(location,text):
        #找到元素位置点击，然后清除输入框，并输入账号密码
        location.Click()
        location.SendKeys('{Ctrl}a{Delete}')
        if text:
            location.SendKeys(text)
    @staticmethod
    def wait_for_exist(control, timeout):
        """等待Control出现, 出现可返回True,否则在timeout后返回False"""
        return uiautomation.WaitForExist(control, timeout)

    @staticmethod
    def wait_for_disappear(control, timeout):
        """等待Control消失，消失可返回True,否则在timeout后返回False"""
        return uiautomation.WaitForDisappear(control, timeout)

def config_server_address(ip,port,pulisher):
    pass

def login_isli_fast(username,password):
    '''
    :param username:
    :param password:
    :return: None
    '''
    #启动程序放在用例的setUP中启动
    #PublicMethod.start_process_fast()
    #实例化elements模块里的Login
    login_element = elements.LoginWindow()
    # 输入信息函数【完成清空并发送账号，清空并发送密码】
    PublicMethod.input(login_element.username_edit,username)
    PublicMethod.input(login_element.password_edit,password)
    # 点击登录按钮
    login_element.login_button.Click()

def logout():
    logout_elment = elements.LoginSuccessWindow()
    PublicMethod.wait_for_exist(logout_elment.setting_options,3)
    logout_elment.setting_options.Click()
    logout_elment.logout_option.Click()
    logout_elment.logout_yes.Click()
def switch_to_sysmanage():
    '''
    switch to sysmanage,to test some example
    :return:return elments instance
    '''
    #登录成功之后查看元素是否存在，实例化系统管理
    time.sleep(0.5)
    reload(elements)
    sysman_element = elements.SystemManage()
    uiautomation.WaitForExist(sysman_element.chose_user_upgrade,1)
    #切换到系统管理
    sysman_element.system_manage_window.Click()
    return sysman_element

def inter_user_manage():
    sysman_element = elements.SystemManage()
    sysman_element.user_manage_button.Click()
def inter_role_manage():
    pass
def inter_usergroup_manage():
    pass

def add_new_account(new_account,new_account_realname):

    '''
    # #登录成功之后查看元素是否存在，实例化系统管理
    # reload(elements)
    # sysman_element = elements.SystemManage()
    # uiautomation.WaitForExist(sysman_element.chose_user_upgrade,1)
    # #切换到系统管理
     '''
    # sysman_element.system_manage_window.Click()


    #switch_to_sysmanage()
    #switch_to_sysmanage()
    #inter_user_manage()
    sysman_element = elements.SystemManage()
    #点击用户管理
    sysman_element.user_manage_button.Click()
    #点击新增按钮
    sysman_element.add_new_button.Click()
    add_newuser_element = elements.AddNewuserWindow()
    PublicMethod.input(add_newuser_element.username_edit,new_account)
    PublicMethod.input(add_newuser_element.realname_edit,new_account_realname)
    add_newuser_element.role_choice.Click(ratioX=0.9)
    add_newuser_element.first_choice_list.Click(ratioX=0.1)
    add_newuser_element.role_choice.Click()
    add_newuser_element.enter_button.Click()
    reload(elements)


if __name__ == "__main__":
    PublicMethod.start_process_fast()
    login_isli_fast("guohp","123456")
    # print (elements.LoginWindow.account_error_message.Name)
    # PublicMethod.start_process_fast()
    # print('*'*20)
    # user_dic=['test001','test002','test003',
    #           'test004','test005','test006','test007','test008','test009','test010','test011','test012']
    # for i in range(len(user_dic)):
    #     username=user_dic[i]
    #     login_isli_fast(username,'123456')

    switch_to_sysmanage()
    #add_new_account('test000001','测试00001')
    #assertTrue(sysman_is_exist,msg='未找到用户信息窗口，没有登录成功')
    #operation.logout()
    #PublicMethod.start_process_fast()
    t=input("-"*20)
    logout()