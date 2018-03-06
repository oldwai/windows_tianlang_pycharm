
# -*- coding:utf-8 -*-
"""
@author:oldwai
"""
# email: frankandrew@163.com

import pyocr
from PIL import Image
from pytesseract import image_to_string, pytesseract

pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR'

# 空白背景色 pytesseract 无法识别，更换了一下背景色
def change_background(img_fp):
    try:
        img = Image.open(img_fp)
        x, y = img.size
        new_img = Image.new('RGBA', img.size, (255, 255, 255))
        new_img.paste(img, (0, 0, x, y), img)
        return new_img
    except:
        print(u'更换图片背景失败')

# 识别图片验证码
def ocr2str(img):
    return str(image_to_string(img))


im = 'G:\\222222222\\code.png'
# 验证码
# code = ocr2str(change_background(im))
img = Image.open(im)
x, y = img.size
new_img = Image.new('RGBA', img.size, (255, 255, 255))
new_img.paste(img, (0, 0, x, y), img)