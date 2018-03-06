# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

class HomePage:
    css_login_button = ('css','div.for_system>span')
    xpath_login_window =('xpath', '//div[@class="for_system"]/span')
    xpath_login_name=('xpath','//input[@id="loginName"]')
    xpath_login_password=('xpath','//input[@id="loginPassword"]')
    xpath_remeber_pwd = ('xpath','//input[@type = "checkbox"]')
    xpath_confirm_login = ('xpath','//button[@type="button"]')
    xpath_setting = ('xpath','//div[@class="for_system"]')
    xpath_fast = ('xpath','//a[@class="softs_logo8"]')

class Setting():
    pass

class AccountManageSet():
    """
    本根服务器RCS账号管理界面元素
    """
    byname_account_manage = ('name','account')
    css_roles_manage = ('css','a[routerlink="/setting/role"]')
    css_add_newaccount = ('css','div.logs>button')
    css_account_loginname = ('css','#account_loginName')
    css_account_realname = ('css','#account_username')
    css_account_password = ('css','#account_password')
    css_account_mobile = ('css','#account_mobile')
    css_account_email = ('css','#account_mail')
    css_submit_button = ('css','button[class$="submit"]')
    css_cancel_button = ('css','button[class$="cancel"]')
    #p-dropdown标签的属性[formcontrolname="selectedRoles"]
    #p-dropdown > div > div:nth-child(2) > input  要确定div标签是唯一的
    css_system_roles = ('css','> p-dropdown > div > div:nth-child(5) > div.ui-dropdown-items-wrapper > ul')
    css_select_roles = ('css','p-dropdown>div>')
    xpath_system_roles = ('xpath','//p-dropdown')

    css_assign_roles = ('css','#vgnbcfgtr1')
    css_modify_account = ('css','#vgnbcfgtr2')
    css_reset_password = ('css','#vgnbcfgtr3')
    css_frozen_account = ('css','#vgnbcfgtr4')
    css_delete_account = ('css','#vgnbcfgtr5')

class RolesManageSet():
    css_roles_manage = ('css','a[routerlink="/setting/role"]')
    css_add_newroles = ('css','button[class$="new_role"]')
    css_fast_permission ='''#mCSB_5_container > p-tree > div > ul > p-treenode:nth-child(8)\
     > li > div > span.ui-treenode-label.ui-corner-all > span > span '''
    css_roles_name = ('css','input[name="roleName"]')
    css_roles_description = ('css','input[name="roleDesc"]')
    css_save_roles = css_add_newroles


if __name__ =="__main__":
    import rcs_operation
    from rcs_operation import login_rcs
    from selenium import  webdriver
    username = "xitest025@163.com"
    password = "a123456"
    RCS_URL = "https://172.16.3.251:9443/#/systemStart"
    rcs_operation.login_rcs(username,password,RCS_URL)


