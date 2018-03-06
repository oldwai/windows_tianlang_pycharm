# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


import re
numRegex = re.compile(r'[Alice|Bob|Carol]')

a = numRegex.search('asdasdasdCarol')
print(a.groups())
