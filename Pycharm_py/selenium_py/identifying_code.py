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
driver.save_screenshot('f://aa.png')  #截取当前网页，该网页有我们需要的验证码
imgelement = driver.find_element_by_xpath('//img[@alt]')  #定位验证码
location = imgelement.location  #获取验证码x,y轴坐标
print location
size=imgelement.size  #获取验证码的长宽
print size
rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
print rangle
i=Image.open("f://aa.png") #打开截图
frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
#frame4.save('f://frame4.jpg')

'''
# def rgb(im):
#     获取每一个像素的亮度     (r+g+b)/3
#     import numpy as np
#     import pandas as pd
#     width, heigth = im.size
#     data = np.zeros((heigth,width))
#     aa = []
#     for w in range(width):
#         for h in range(heigth):
#
#             y,cb,cr=im.getpixel((w,h))
#             data[h,w] = (y+cb+cr)/3
#             aa.append((y+cb+cr)/3)
#     data = pd.DataFrame(data)
#     aa = pd.Series(aa)
#     return aa,data
#
# def topliangdu(liangdu, biaozhun=100):
#     根据亮度排序，取大于标准的值
#     c=liangdu.value_counts()
#     return list(c[c>100].index)
#
# def liangdutianbai(im,mubiao):
#     将非目标区域填充白色
#     width, heigth = im.size
#     for w in range(width):
#         for h in range(heigth):
#             y,cb,cr=im.getpixel((w,h)) #提取点(10,10)位置的亮度、蓝色分量、红色分量的值。
#             tmp = (y+cb+cr)/3
#             if tmp not in mubiao:
#                 im.putpixel([w,h],(255, 255, 255))
#     return im
#
# def tongse(im):
#     验证码验证文字的单个文字同色时，处理。
#     global aa, data
#     aa,data = rgb(im)
#     mubiao = topliangdu(aa)
#     im = liangdutianbai(im, mubiao)
#     img_grey = im.convert('L')
#     img_grey.show()
#    return img_grey
'''


# qq=Image.open('f://frame4.jpg')
# sleep(2)
# #text=pytesseract.image_to_string(qq).strip()#使用image_to_string识别验证码
# text = pytesseract.image_to_string(qq)  # 将图片转成字符串
# print text