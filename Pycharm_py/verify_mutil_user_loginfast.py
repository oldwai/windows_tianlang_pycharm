# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

import uiautomation
import subprocess
import time

class LoginWindows:
    #登录界面主窗口
    root_window = uiautomation.PaneControl(searchDepth=1, ClassName='Qt5QWindow')
    #登录窗口
    login_root_window = root_window.CustomControl(searchDepth=1, Name='')
    auto_login=login_root_window.CheckBoxControl(searchDepth=1, Name='自动登录')
    remember_passwd = login_root_window.CheckBoxControl(searchDepth=1, Name='记住密码')
    username_edit=login_root_window.EditControl(searchDepth=1, foundIndex=1)
    password_edit=login_root_window.EditControl(searchDepth=1, foundIndex=2)
    login_button=login_root_window.ButtonControl(searchDepth=1, Name='登 录')
    #错误提示语获取
    account_error_location=login_root_window.TextControl(foundIndex=2)
    #account_error_message=account_error_location.Name
    #服务器设置
    server_config=login_root_window.ButtonControl(foundIndex=1, searchDepth=1)

def input(location,text):
        #找到元素位置点击，然后清除输入框，并输入账号密码
        location.Click()
        location.SendKeys('{Ctrl}a{Delete}')
        if text:
            location.SendKeys(text)
def start_process_fast():
        subprocess.Popen("C:\\Program Files (x86)\\MPRTimes\\ISLI FAST\\ISLI FAST.exe")
        root_window = uiautomation.PaneControl(searchDepth=1, ClassName='Qt5QWindow')
        # uiautomation.WaitForExist(root_window, 1)
        root_window.ShowNormal()  # 激活显示
        root_window.SetWindowTopmost(True)  # 置顶显示

def login_isli_fast(username,password):
    '''
    :param username:
    :param password:
    :return: None
    '''
    #启动程序放在用例的setUP中启动
    #PublicMethod.start_process_fast()
    #实例化elements模块里的Login
    login_element = LoginWindows()
    # 输入信息函数【完成清空并发送账号，清空并发送密码】
    input(login_element.username_edit,username)
    input(login_element.password_edit,password)
    # 点击登录按钮
    login_element.login_button.Click()


if __name__=='__main__':
    start_process_fast()
    #login_isli_fast('caolh','123456')
    user_dic=['test001','test002','test003',
              'test004','test005','test006','test007','test008','test009','test010','test011','test012']
    for i in range(len(user_dic)):
        username=user_dic[i]
        login_isli_fast(username,'123456')