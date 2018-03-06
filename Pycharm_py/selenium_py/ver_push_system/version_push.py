#coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver
from time import sleep
from selenium.common.exceptions import InvalidSelectorException

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

#添加cookie
#driver.add_cookie({'name':'JSESSIONID','value':'182441EC456A9EE91328D9E17A3D0080'})
#driver.add_cookie({'name':'jsessionid','value':'182441EC456A9EE91328D9E17A3D0080'})

#刷新页面
#driver.refresh()

#清空再输入用户名/密码
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys(login_name)
driver.find_element_by_name("pwd").clear()
driver.find_element_by_name("pwd").send_keys(login_pwd)
sleep(10)

#点击登录界面
driver.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']").click()
#driver.find_element_by_xpath("/html/body/div/app-root/div/tl-publish-login/div/div/p-panel/div/div[2]/div/form/div[4]/button").click()
'''
try:
    element=driver.find_element_by_class_name('btn btn-primary btn-sm')
except InvalidSelectorException as msg:
    print u"查找元素异常%s"%msg
else:
    element.click()

'''

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
upgrade_button1.send_keys(fast_client_path)
#下面的路径执行不行
#driver.find_element_by_xpath("//div[contains(@class,'form-control control-cont upload-btn')]").click()

#版本号输入框位置
#/html/body/div/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[3]/input
#.form-control.control-cont.ng-pristine.ng-invalid.ng-touched
#xpath定位：//input[contains(@class,'form-control control-cont ng-pristine ng-invalid ng-touched')]
sleep(10)
version_num=driver.find_element_by_xpath("/html/body/div/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[3]/input")
version_num.send_keys("V2.1.0.6557")

#版本特性输入框位置
#version_attribute=driver.find_element_by_xpath
# ("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[4]/div[2]/div/div/textarea")
version_attribute=driver.find_element_by_xpath("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[4]/div[2]/div/div/textarea")
version_attribute.send_keys("auto_test")



sleep(10)
#提交审核按钮定位
submit_button=driver.find_element_by_xpath("//button[@class='btn btn-success']")
#sleep(2)
submit_button.click()
#driver.quit()

