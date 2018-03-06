# -*- coding:utf-8 -*-
"""
@author:oldwai
"""
# email: frankandrew@163.com

import requests


class RmsPushVersion():
    def __init__(self):
        self.host = 'http://172.16.3.112:51117'
        self.s = requests.Session()
        self.jsessionid = self.get_sessionid()

    def get_url(self, endpoint):
        url = self.host + endpoint
        return url

    def get_sessionid(self):
        # 获取sessionid的url才用get方法
        endpoint = '/versionserver/user/newValidCode'
        url = self.get_url(endpoint)
        r = self.s.get(url)
        sessionid = r.json()['data']['sessionId']
        return sessionid

    def publish_login(self):
        endpoint = '/versionserver/user/login;jsessionid={0}' \
            .format(self.jsessionid)
        url = self.get_url(endpoint)
        data = {
            'username': '457815031@qq.com',
            'password': 'tianlang123456',
            'userType': '2',
            'codeCon': '1234'
        }
        r = self.s.post(url,data=data)
        print(r.json())
        print(self.jsessionid)

    def upload_file(self):
        endpoint = '/versionserver/version/uploadFile;jsessionid={0}' \
            .format(self.jsessionid)
        url = self.get_url(endpoint)
        pic_path = '1'
        files = {'file': open(pic_path, 'rb')}
        r = self.s.post(url=url, files=files, verify=False)

    def push_newversion(self):
        endpoint = '/versionserver/version/newVersion;jsessionid={0}' \
            .format(self.jsessionid)
        url = self.get_url(endpoint)
        json_data = {"productId": 2, "updateType": 1, "policyType": 0,
                     "client": {"systemName": "FAST_client_win",
                                "lastVersionNum": "V2.2.0.6846",
                                "versionNum": "V2.2.0.6848",
                                "changeContent": "1111111111111接口:  \n",
                                "note": "111111接口",
                                "fileUuid": "500db659-f18a-499a-9438-e21e342106a9",
                                "fileMd5": "db0c3199b1f50255c947b7c4082fd212",
                                "attachFileUuid": "",
                                "compatibility": 0,
                                "rel": ""},
                     "server": {},
                     "policyList": [{"targetUser": "0",
                                     "region": "86",
                                     "pushTime": "2018-02-23 00:00:00"}]}
        r = self.s.post(url=url, json=json_data, verify=False)


if __name__ == '__main__':
    test = RmsPushVersion()
    test.publish_login()