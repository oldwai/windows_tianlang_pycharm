# -*- coding:utf-8 -*-
"""
@author:oldwai
"""
# email: frankandrew@163.com

from PIL import Image,ImageEnhance
from pytesseract import image_to_string


# def parse(self,response):
#
#     ret=response.xpath('//*[@id="codePic"]/@src').extract()
#
#     image_source=ret[0]
#
#     image_url=response.urljoin(image_source)
#
#     r=requests.get(image_url)
#
#     with open('E://scrapy_project/image2.JPEG',"wb") as code:
#
#         code.write(r.content)

im = Image.open('G:\\222222222\\code.png')

imgry = im.convert('L')

ret = image_to_string(im, config='-psm 7')
print(ret)
