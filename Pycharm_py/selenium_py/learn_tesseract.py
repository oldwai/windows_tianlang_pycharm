#coding:utf-8
'''
@author:oldwai
'''


from selenium import webdriver
import win32gui
import win32con
from time import sleep

#发布中心的地址
pub_site_url= "http://172.16.3.112:8080/versionserver/static/index.html#/publish/login"
login_name="457815031@qq.com"
login_pwd="tianlang123456"
fast_client_path="D:\\database_creation.sql"
#u"\\\172.16.6.4\\RD_Center\\17 公司自主开发软件安装包\\MPR FAST\\V2.1.0.svn\\Client\\20170719 93054_V2.1.0.6556"

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get(pub_site_url)
print (driver.get_cookies())
sleep(2)


#清空再输入用户名/密码
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys(login_name)
driver.find_element_by_name("pwd").clear()
driver.find_element_by_name("pwd").send_keys(login_pwd)
sleep(10)

#点击登录界面
driver.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']").click()
#driver.find_element_by_xpath("/html/body/div/app-root/div/tl-publish-login/div/div/p-panel/div/div[2]/div/form/div[4]/button").click()

sleep(3)
print(driver.get_cookies())

#已经登录成功，切换到版本发布中心页面
#driver.find_element_by_link_text(u'版本发布').click()

driver.find_element_by_link_text(u'版本发布').click()
driver.find_element_by_xpath("//button[@class='btn btn-primary btn-w']").click()

sleep(10)
#产品升级包的xpath路径
#upgrade_path="/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[6]/input[2]"
upgrade_button1=driver.find_element_by_xpath("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[6]/input[2]")
sleep(2)
upgrade_button1.click()


# win32gui
dialog = win32gui.FindWindow('#32770', u'文件上传') # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None) # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None) # 确定按钮Button

win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\baidu.py') # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 按button


#版本号输入框位置
#/html/body/div/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[3]/input
#form-control control-cont ng-pristine ng-invalid ng-touched
#css定位：//input[contains(@class,'form-control control-cont ng-pristine ng-invalid ng-touched')]
version_num=driver.find_element_by_xpath("/html/body/div/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[3]/input")
version_num.send_keys("V2.1.0.6557")
#版本特性输入框位置
#version_attribute=driver.find_element_by_xpath
# ("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[4]/div[2]/div/div/textarea")
version_attribute=driver.find_element_by_xpath("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[4]/div[2]/div/div/textarea")
version_attribute.send_keys("auto_test")
sleep(1)

sleep(10)

#提交审核按钮定位
submit_button=driver.find_element_by_xpath("//button[@class='btn btn-success']")
#sleep(2)
submit_button.click()
#driver.quit()