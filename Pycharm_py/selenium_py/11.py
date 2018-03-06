#coding:utf-8
'''
@author:oldwai
'''

from selenium import webdriver
from time import sleep
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.support.wait import WebDriverWait

#获取登录信息
#def login_info():


#浏览器选择

#登录版本推送系统
def login_verpush_sys(url,username,pwd):
    global driver
    driver.get(url)
    sleep(2)
    #定位--输入用户名密码框
    path_name_frame=driver.find_element_by_name("user")
    path_passwd_frame=driver.find_element_by_name("pwd")
    #定位--登录按钮框
    path_login_button=driver.find_element_by_xpath("//button[@class='btn btn-primary btn-sm']")
    path_identify_code=driver.find_element_by_name("ValidCode")
    path_name_frame.clear()
    path_name_frame.send_keys(username)
    path_passwd_frame.clear()
    path_passwd_frame.send_keys(pwd)
    identify_code=raw_input("请输入正确的验证码：")
    #获取登录之前的URL
    login_url=driver.current_url
    sleep(5)
    path_identify_code.send_keys(identify_code)
    path_login_button.click()
    #获取点击登录之后的URL
    login_success_url=driver.current_url
    return login_url,login_success_url

#发布客户端版本
def client_upgrade(url='http://172.16.3.112:8080/versionserver/static/index.html#/publish/login',username="457815031@qq.com",pwd="tianlang123456"):
    #login_verpush_sys()
    # 定位--版本发布链接按钮
    login_verpush_sys(url,username,pwd)
    sleep(2)
    path_ver_push_href=driver.find_element_by_link_text(u'版本发布')
    path_ver_push_href.click()
    # 定位--版本发布按钮
    path_ver_push_button=driver.find_element_by_xpath("//button[@class='btn btn-primary btn-w']")
    #进入到发布客户端版本页面
    path_ver_push_button.click()
    sleep(2)
    # 定位--选择客户端
    path_choose_client_path_button=driver.find_element_by_xpath("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[6]/input[2]")
    # 定位--输入版本信息
    path_input_client_verinfo=driver.find_element_by_xpath("/html/body/div/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[3]/input")
    # 定位--提交审核按钮
    path_submit_button=driver.find_element_by_xpath("//button[@class='btn btn-success']")
    #定位到版本特性
    version_attribute=driver.find_element_by_xpath("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[4]/div[2]/div/div/textarea")
    #提交审核按钮
    path_submit_button=driver.find_element_by_xpath("//button[@class='btn btn-success']")

    #选择客户端版本并输入相应信息
    client_verinfo=raw_input("请输入客户端版本信息（格式如V2.1.0.6455）：")
    path_input_client_verinfo.send_keys(client_verinfo)
    version_attribute.send_keys(client_verinfo)
    #还要输入版本说明信息
    #upgrade_client_path=(raw_input("请输入升级的绝对路径：")
    upgrade_client_path=("D:\\ISLI_FAST_Upgrade\\ISLI FAST_Setup_x86.exe")
    path_choose_client_path_button.send_keys(upgrade_client_path)
    publish_web_url=driver.current_url
    print "这是发布的时的URL：",publish_web_url
    sleep(2)
    path_submit_button.click()
    sleep(10)
    publish_success_url=driver.current_url
    driver.close()
    #sleep(10)
    #driver.find_element_by_class_name("logout-btn").click()
    # if publish_success_url=="http://172.16.3.112:8080/versionserver/static/index.html#/publish/version/list":
    #     print("发布成功")
    #     driver.find_element_by_class_name("logout-btn").click()
    # else:
    #     print("发布失败")


#验证是否登录成功
def verify_login_success(url_list):
    if url_list[0]==url_list[1]:
        print("登录失败，请检查原因：")
    else:
        print("登录成功")

#发布服务端版本
def server_upgrade():
    #login_verpush_sys()
    # 定位--版本发布链接按钮
    path_ver_push_href=driver.find_element_by_link_text(u'版本发布')
    path_ver_push_href.click()
    # 定位--版本发布按钮
    path_ver_push_button=driver.find_element_by_xpath("//button[@class='btn btn-primary btn-w']")
    #进入到发布客户端版本页面
    path_ver_push_button.click()
    sleep(2)
    # 定位--选择客户端
    path_choose_client_path_button=driver.find_element_by_xpath("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[6]/input[2]")
    # 定位--输入版本信息
    path_input_client_verinfo=driver.find_element_by_xpath("/html/body/div/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[3]/input")
    # 定位--提交审核按钮
    path_submit_button=driver.find_element_by_xpath("//button[@class='btn btn-success']")
    #定位到版本特性
    version_attribute=driver.find_element_by_xpath("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[4]/div[2]/div/div/textarea")

    #选择客户端版本并输入相应信息
    server_verinfo=raw_input("请输入服务端版本信息（格式如V2.1.0.6455）：")
    path_input_client_verinfo.send_keys(server_verinfo)
    version_attribute.send_keys(server_verinfo)
    #还要输入版本说明信息
    #upgrade_client_path=(raw_input("请输入升级的绝对路径：")
    upgrade_Linux_server_path=("\\\172.16.6.4\\RD_Center\\17 公司自主开发软件安装包\\MPR FAST\\Trunk\\Client\\20170726105158_V2.1.0.6577")#("D:\\ISLI_FAST_Upgrade\\ISLI FAST_Setup_x86.exe")
    path_choose_client_path_button.send_keys(upgrade_Linux_server_path)

#版本发布审核
def release_upgrade(url='http://172.16.3.112:8080/versionserver/static/index.html#/release/login',username="caolh@mpreader.com",pwd="tianlang123456"):
    login_verpush_sys(url,username,pwd)
    sleep(3)
    #版本管理链接按钮
    version_manger_path=driver.find_element_by_link_text("版本管理")
    version_manger_path.click()
    sleep(1)
    #产品英文缩写
    query_product_info=driver.find_element_by_id("acronymviation")
    #查询按钮
    query_btn=driver.find_element_by_xpath("//button[@type='submint']")

    #输入要查询的产品的英文缩写，如：FAST
    your_product=raw_input("------请输入你要查询的产品名称，英文缩写----：")
    query_product_info.send_keys(your_product)
    sleep(2)
    query_btn.click()
    sleep(2)
    #审核按钮
    confirm=driver.find_element_by_link_text("审核")
    confirm.click()
    sleep(2)
    #确定发布页面的审核按钮
    confirm2=driver.find_element_by_xpath("/html/body/div/app-root/div/tl-manage-version/tl-version-detail/div/div[3]/div/button[1]")
    confirm2.click()
    sleep(2)
    rightnow_push=driver.find_element_by_xpath("/html/body/div[1]/app-root/div/tl-manage-version/tl-version-detail/p-dialog/div/p-footer/div/button[2]/span[2]")
    rightnow_push.click()


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
#版本升级地址和登录信息和升级安装包绝对路径
ver_push_url='http://172.16.3.112:8080/versionserver/static/index.html#/publish/login'
ver_release_url='http://172.16.3.112:8080/versionserver/static/index.html#/release/login'
push_login_name="457815031@qq.com"
release_login_name="caolh@mpreader.com"
push_login_pwd="tianlang123456"
#需要解决如何填写共享路径
#upgrade_client_path="\\\172.16.6.4\\RD_Center\\17 公司自主开发软件安装包\\MPR FAST\\Trunk\\Client\\20170724234647_V2.1.0.6569\\ISLI FAST_Setup_x86.exe"

#调用login函数，打开升级地址，输入用户名密码登录

#发布客户端版本
client_upgrade()


release_upgrade()
#登录审核地址
#release_upgrade(ver_release_url,release_login_name,push_login_pwd)
#driver.quit()
#sleep(2)
#登录审核地址
#login_verpush_sys(ver_push_url,release_login_name,push_login_pwd)




