# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

import os, sys
from PIL import Image

image = Image.open('test.jpg')

image = image.rotate(60,translate='left')

image.show()