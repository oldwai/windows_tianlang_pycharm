#coding:utf-8
'''
@author:oldwai
'''

import requests

url = "https://172.16.3.251:8443/mpr/portal-rms-api/mvc/sysManager/login"

#payload = "{\"loginName\":\"caoleihua\",\"password\":\"123456\",\"test\":\"123\"}"
payload = '{"loginName":"caoleihua","password":"123456","test":"123"}'
headers = {
    'authorization': "Basic cG9zdG1hbjpwYXNzd29yZA==",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "100485f1-53b4-be95-747a-fbd71724ad10"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

test=dict(response.text)
print(response.text)
for key in test.items():
    print key
    if key=="msg":
        print test[key]
