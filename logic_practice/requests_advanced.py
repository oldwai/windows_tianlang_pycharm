# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


import requests


host = "https://www.baidu.com/s"
s = requests.Session()
header1 = {'test11':'111'}
header2 = {'test22':'222'}
s.headers.update(header1)
requests.session()

r = s.get(host, headers=header2, verify=False)
print(r.headers)