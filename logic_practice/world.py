# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

import datetime
import glob
import json
import random
import time

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3


class MprWorld:
    def __init__(self, account, passwd):
        self.s = requests.Session()

        self.host = 'http://172.16.3.45:11999/'
        self.account = account
        self.passwd = passwd

        # requests库请求HTTPS时,因为忽略证书验证,会有警告，这里禁止警告
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        urllib3.disable_warnings()
        self.user_id = self.login()

    def login(self):
        """
        登录函数，以字符串的形式返回user_id，方便其他操作调用user_id
        :return: 返回user_id
        """
        post_data = {"p_version": "1",
                     "terminal_serial": "ccc275b6-32a7-35c4-a1db-a707026952af",
                     "terminal_type": "ZOPO-M561",
                     "phone_number": self.account,
                     "password": self.passwd}
        login_url = self.host + 'api/aaa/login/fm'
        DataAll = {'json': post_data}
        r = self.post_response(login_url, **DataAll)
        if r['return_code'] == '0':
            print('登录成功！')
        else:
            print(r['status'])
        # 登录会返回一个user_id,和一个session, seesion会作为Cookie在后面的头信息用到,下面将Cookie添加到会话中
        self.s.headers.update({'Cookie': 'ifm_sid=%s' % r['status']['session']})
        return str(r['status']['user_id'])


if __name__ == "__main__":
    s = requests.Session()
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.7.1 Chrome/49.0.2623.111 Safari/537.36",
        "token": "eyJhbGciOiJIUzUxMiJ9.eyJhdWQiOiIxNzIuMTYuNy41NSIsInRpY2tldCI6IkM3Njc5Mzc4LThEMTctNDM4MS05MTIwLUZEODVFNkZDNzBFQyIsInVuaWZpY2F0aW9uSWQiOjE1MTcyNzk3Nzc4MjQzNzM4LCJicmFuZElkIjoiMDAwMDAwMDIiLCJpc3MiOiI2NUNGNkQ0NkIzRjQ0RTE0QUFDRDM1REQ2NTIyNUQwNiIsInJlcXVlc3RJcCI6IjE3Mi4xNi43LjU1IiwiZXhwIjoxNTE3MzkzNzA2LCJkZXZpY2VJZCI6IjAwMDAwMDAyZWFlZjYzM2QwMGQyMTFlMzk1ZTA5YThjZWUwNzU0OTIiLCJpYXQiOjE1MTczOTE5MDYsImp0aSI6IjliMWJhOTNjZjBiNjQ5NjY4NDAxYzJkOGQ2MGMzYWViIn0.GZiC8m3a2VnzMSb_x5txui3ZYgOqgf90Gc2nbcrhn1llW7QBXqR4oOfvqv_mi8XU60HWruBm3FJIOQtcI8WzEw"
    }
    json = {"id":"1191",
            "userEmail":"huangwq@mpreader.com",
            "nickName":'<a title="popper.w" onclick="alert(1)">popper.w" onclick="alert(1)</a>',
            "userPhone":"13232323222",
            "userSex":0,
            "birthDay":"2018-12-31",
            "location":{"country":"0",
                        "province":"3853",
                        "city":"3868",
                        "area":"3872"},
            "userImage":"http://172.16.3.45:11999/file/image/2018/02/xn7krelftbzn4r31zsu9/tn8iq7ujaiuqe3hbblte.jpeg"}
    # json = {"goodsType": "0", "shopId": "1402", "goodsId": "916",
    #         "goodsPrice": "0.01", "number": 1}
    save_uereinfo_url = "http://172.16.3.45:11999/pcs/v1/user-center/user/info"
    # url = "http://172.16.3.45:11999/pgsp/v1/goods/find?parentClassification=1&pageIndex=1&pageRows=100"
    # url2 = "http://172.16.3.45:11999/pcs/v1/buycar/add"
    r = s.put(save_uereinfo_url, headers=headers, json=json, verify=False)
    print(r.text)
    # #print(r.json())
    # list1 = []
    # print(r.status_code)
    # if r.status_code =="200":
    #     #print(r.status_code)
    #     for dic in r.json()["data"]["pageDataList"]:
    #         id_price = {k: v for k, v in dic.items() if (
    #             k in ["goods_id", "goods_price", "goods_name", "shop_id"])}
    #         # == "goods_id" or k == "goods_price" or k =="goods_name" or )}
    #         goodsId = id_price["goods_id"]
    #         goodsPrice = id_price["goods_price"]
    #         goods_name = id_price["goods_name"]
    #         #print(goodsId, goodsPrice, goods_name)
    #         #for i in range(1,999999990):
    #         data = {"goodsType": "0", "shopId": "1402", "goodsId": goodsId,
    #                 "goodsPrice": goodsPrice, "number": 1}
    #         #time.sleep(1)
    #         r = s.post(url2, headers=headers, json=data)
    #         time.sleep(1)
    #         print(r.text)
    #         # print(goodsId,goodsPrice,r.status_code)
    #         # list1.append(id_price["shop_id"])
    #         list1.append(id_price)
    # print(len(list1))
