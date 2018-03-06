#coding:utf-8
'''
@author:oldwai
'''


from PIL import Image
import pytesseract
from selenium import webdriver
from time import sleep

url='http://172.16.3.112:8080/versionserver/static/index.html#/publish/login'
driver = webdriver.Chrome()
#driver.maximize_window()  #将浏览器最大化
driver.get(url)
#for j in range(30,1000):
    j+=1
    driver.save_screenshot('f://aa.png')  #截取当前网页，该网页有我们需要的验证码
    imgelement = driver.find_element_by_xpath('//img[@alt]')  #定位验证码
    location = imgelement.location  #获取验证码x,y轴坐标
    size=imgelement.size  #获取验证码的长宽
    rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
    i=Image.open("f://aa.png") #打开截图
    frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
    Low=frame4.convert('L')
    Low=frame4.convert('1')
    Low.save("D:\\version_pic\\Low\\%d.jpg"%j)
    driver.refresh()
    sleep(3)
