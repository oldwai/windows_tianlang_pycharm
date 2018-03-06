# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email:frankandrew@163.com

import requests

url = "http://localhost.:8000/admin/sign/event/add/"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nautotest\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"limit\"\r\n\r\n111\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"address\"\r\n\r\n111\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"start_time_0\"\r\n\r\n2018-01-15\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"start_time_1\"\r\n\r\n01:50:32\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"_save\"\r\n\r\nSave\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'host': "localhost.:8000",
    'connection': "keep-alive",
    'content-length': "821",
    'cache-control': "no-cache",
    'postman-token': "779db4e9-597c-b824-c888-3426f467cb37"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

#("http://localhost.:8000/admin/sign/event/add/",data=payload,headers=headers,verify=False)