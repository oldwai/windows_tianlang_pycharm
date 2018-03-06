#coding:utf-8
'''
@author:oldwai
'''

from Ver_push_sys_BasePage import Ver_push_sys_Basepage
from selenium.webdriver.common.by import By


class Release_Version_page():
    release_version_href=(By.LINK_TEXT,u'版本发布')
    #客户端上次版本号

    #客户端本次版本号
    xpath_client_version_num=("/html/body/div/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[3]/input")
    client_version_num=(By.XPATH,xpath_client_version_num)
    #客户端版本特性
    xpath_version_attribute=("/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[4]/div[2]/div/div/textarea")
    version_attribute=(By.XPATH,xpath_version_attribute)
    #客户端路径信息按钮
    xpath_client_choose_button="/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[6]/input[2]"
    client_choose_button=(By.XPATH,xpath_client_choose_button)
    absolute_path="\\\172.16.6.4\RD_Center\\17 公司自主开发软件安装包\\MPR FAST\\Trunk\\Client\\20170806234559_V2.1.0.6620\\ISLI FAST_Setup_x86.exe"
    #md5值
    xpath_md5="/html/body/div[1]/app-root/div/tl-publish-product/tl-product/div/div[2]/div/tl-product-software/form/div[2]/tl-product-software-client/div/div[7]/input"
    md5_button=(By.XPATH,xpath_md5)
    #提交审核按钮
    xpath_submit_button="//button[@class='btn btn-success']"
    submit_button=(By.XPATH,xpath_submit_button)
    #click
    #def __init__(self,driver):
       # self.driver=driver

    def click_release_button(self):
        release_button=self.driver.find_element(*Release_Version_page.release_version_href)
        release_button.click()
        return self.driver

    def release_client(self):
        client_path=self.driver.find_element(*Release_Version_page.client_choose_button)
        client_path.send_keys(Release_Version_page.absolute_path)
        md5_check=self.driver.find_element(*Release_Version_page.md5_button)
        attribute=md5_check.get_attribute("value")
        while attribute:
            version_info=raw_input("请输入本次发布的版本号，格式如--V2.0.0.111:")
            client_version_num_conf=self.driver.find_element(*Release_Version_page.client_version_num)
            client_version_num_conf.send_keys(version_info)
            version_attribute_conf=self.driver.find_element(*Release_Version_page.version_attribute)
            version_attribute_conf_input=raw_input("请输入版本特性：")
            version_attribute_conf.send_keys(version_attribute_conf)
            submit_button_conf=self.driver.find_element(*Release_Version_page.submit_button)
            submit_button_conf.click()

    #def release_server(self):




