#coding:utf-8
'''
@author:oldwai
'''
import uiautomation

class LoginWindow:
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

class LoginSuccessWindow:
    #登录后的主窗口
    root_window=uiautomation.PaneControl(searchDepth=1,ClassName='Qt5QWindowIcon')
    #最上排元素位置
    top_location=root_window.CustomControl(searchDepth=1,foundIndex=1)
    #聊天窗口
    chat_box=top_location.ButtonControl(Name='')
    #用户消息
    user_message=top_location.CustomControl(foundIndex=2,Name='')
    #设置
    account_info=top_location.CustomControl(foundIndex=3)
    setting_options=account_info.MenuItemControl()
    #点击设置后会弹出框，变为主窗口，ClassName为Qt5QWindowPopupDropShadowSaveBits，ControlType=MenuControlTypeId
    setting_root_window=uiautomation.MenuControl(ClassName='Qt5QWindowPopupDropShadowSaveBits')
    #设置里的选项
    options=setting_root_window.MenuItemControl(Name='选项')
    #修改密码
    change_pwd_option=setting_root_window.MenuItemControl(Name='修改密码')
    #帮助手册
    help_manual=setting_root_window.MenuItemControl(Name='帮助手册 F1')
    #意见反馈
    feedback=setting_root_window.MenuItemControl(Name='意见反馈')
    #关于选项
    about_option=setting_root_window.MenuItemControl(Name='关于')
    #退出选项
    logout_option=setting_root_window.MenuItemControl(Name='退出')
    #是否退出当前账号弹框
    confirm_to_quit=root_window.PaneControl(ClassName='Qt5QWindow',foundIndex=1)
    logout_yes=confirm_to_quit.ButtonControl(Name='是 Enter')
    logout_no=confirm_to_quit.ButtonControl(Name='否')
    #fast皮肤设置
    window_skin_setting=top_location.CustomControl(foundIndex=6)
    #fast窗口大小、关闭设置
    setting_window=top_location.CustomControl(foundIndex=5)
    min_window_fast=setting_window.ButtonControl(foundIndex=1)
    max_window_fast=setting_window.ButtonControl(foundIndex=2)
    close_window_fast=setting_window.ButtonControl(foundIndex=3)
class Workflow:
    pass
class SystemManage:
    #新的主窗口，重新定义
    sysmanage_root_window=uiautomation.PaneControl(searchDepth=1,ClassName='Qt5QWindowIcon')
    #系统管理层级
    index2_root_windows=sysmanage_root_window.CustomControl(searchDepth=1,foundIndex=2,Name='')
    #角色、用户管理栏定位框的父级
    index_1_i2_root_windows=index2_root_windows.CustomControl(searchDepth=1,foundIndex=1)
    #新增栏定位父级框
    index_2_i2_root_windows=index2_root_windows.CustomControl(searchDepth=1,foundIndex=2)
    #用户管理栏父级框
    chose_user_upgrade=index_1_i2_root_windows.PaneControl()
    #查找系统管理窗口
    x1=index_1_i2_root_windows.CustomControl(searchDepth=4,Name='')
    system_manage_window=x1.RadioButtonControl(Name='系统管理')
    #system_manage_window=sysmanage_root_window.RadioButtonControl(Name='系统管理')
    #用户管理界面
    user_manage_button=chose_user_upgrade.CheckBoxControl(foundIndex=2)
    #新增按钮
    add_new_button=index2_root_windows.ButtonControl(Name='新增')
    #表格窗口


class AddNewuserWindow:
    """点击新增按钮弹框后定位的页面元素"""
    #
    root_window=SystemManage.sysmanage_root_window
    add_user_root_window=root_window.PaneControl(ClassName='Qt5QWindow')
    #新增：用户名输入框
    username_edit=add_user_root_window.EditControl(foundIndex=1,Name='')
    #新增：真实姓名输入框
    realname_edit=add_user_root_window.EditControl(foundIndex=2,Name='')
    #角色
    role_choice=add_user_root_window.ComboBoxControl(Name=' Down')
    role_choice_list=role_choice.ListControl(Name='')
    #第一个选项按钮
    first_choice_list=role_choice_list.ListItemControl(foundIndex=1)
    #确定
    enter_button=add_user_root_window.ButtonControl(Name='确定 Enter')
    #取消
    cancel_button=add_user_root_window.ButtonControl(Name='取消')
    #error 提示语
    error_prompt=add_user_root_window.TextControl()

if __name__ == "__main__":
    # LoginWindow.server_config.Highlight()
    # LoginWindow.server_config.Click()
    # print(LoginWindow.account_error_location.Name)
    # print(type(LoginWindow.account_error_location.Name))
    AddNewuserWindow.add_user_root_window.Highlight()
