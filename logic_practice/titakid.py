# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


import datetime

import requests
import json
import re

from requests.packages.urllib3.exceptions import InsecureRequestWarning


class TiTaKidApp:
    def __init__(self, account, passwd):
        self.s = requests.Session()

        self.host = 'https://api.titakid.com:19000/'
        self.account = account
        self.passwd = passwd
        self.babyId = "129115459335776"
        self.last_url = '?apikey=tinnotech&timestamp=1516086205&sign=5fb839e39ff9d4460facd2f74b91296e'

        # requests库请求HTTPS时,因为忽略证书验证,会有警告，这里禁止警告
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def login(self):
        post_data = {"password":self.passwd,
                     "phone":self.account
                        }
        login_url = self.host + 'smartwatch/member/login' +self.last_url
        print(login_url)
        r = self.s.post(login_url, data=post_data, verify=False)
        # 设置为utf-8编码
        r.encoding = 'utf-8'
        r = r.json()
        if r['errcode'] == '0':
            print('登录成功！')
        else:
            print(r['errmsg'])
        # 登录会返回一个openid,和一个token, token会作为在后面的提交信息,下面将token返回，给其他接口调用
        return str(r['data']['token'])

    def add_contact(self,family_name,family_phone,other_phone):
        post_data = {"portraitId":0,
                     "phone":family_phone,
                     "nickName":family_name,
                     "token":self.login(),
                     "babyId":self.babyId,
                     "otherPhone":other_phone}
        header_agent = "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; ZP720 Build/KTU84P) " \
                       "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36"
        self.s.headers.update({'User-Agent': header_agent})
        add_contact_url = self.host + "smartwatch/baby/addContact" + self.last_url
        r = self.s.post(add_contact_url, data=post_data, verify=False)
        print(r.json())

if __name__ == "__main__":
    login_account = "13277777777"
    login_password = "123456"
    family_name = "auto_interface111"
    family_phone = "13013001301"
    other_phone = "13113001301"
    titakid = TiTaKidApp(login_account,login_password)
    titakid.add_contact(family_name,family_phone,other_phone)