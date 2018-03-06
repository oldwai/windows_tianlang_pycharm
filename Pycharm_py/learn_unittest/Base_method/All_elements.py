#coding:utf-8
#author:oldwai
#email:frankandrew@163.com



class Login_page_element():
    #登录页面的所有元素
    #to locate element by selector by(type,text)
    username=("name,email")
    password=("name,password")
    login_button=("id,dologin")
    login_url=("http://mail.163.com")

class Login_success_page_element():
    login_success_account=("id,spnUid")
    #未读邮件的数量
    unread_mail_num=("id,nui-tree-item-count")