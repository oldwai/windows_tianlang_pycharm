# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class PostFile:
    def __init__(self, account, passwd):
        self.s = requests.Session()

        self.host = 'https://172.16.3.121/'
        self.account = account
        self.passwd = passwd

        # requests库请求HTTPS时,因为忽略证书验证,会有警告，这里禁止警告
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.user_id = self.login()

    def login(self):
        post_data = {"p_version": "1",
                     "terminal_serial": "ccc275b6-32a7-35c4-a1db-a707026952af",
                     "terminal_type": "ZOPO-M561",
                     "phone_number": self.account,
                     "password": self.passwd}
        login_url = self.host + 'api/aaa/login/fm'
        r = self.s.post(login_url, json=post_data, verify=False)
        # 设置为utf-8编码
        r.encoding = 'utf-8'
        r = r.json()
        if r['return_code'] == '0':
            print('登录成功！')
        else:
            print(r['status'])
        # 登录会返回一个user_id,和一个session, seesion会作为Cookie在后面的头信息用到,下面将Cookie添加到会话中
        self.s.headers.update({'Cookie': 'ifm_sid=%s' % r['status']['session']})
        return str(r['status']['user_id'])

    def upload_img(self):
            user_id = self.user_id
            upload_url = 'https://172.16.3.121/api/bookclubserver/isli/image/put'
            param = {'p_version': '1',
                     'goods_id': '201801041052512454',
                     'local_time': '0',
                     'user_id': user_id,
                     'isli_source_id': '151563926401647000',
                     'image_name': '.png'}

            param_json = json.dumps(param)
            payload = {'param_json': param_json}
            files = {'file': open('d:\\screenshot.png', 'rb')}
            r = self.s.post(url=upload_url, data=payload, files=files, verify=False)
            print(r.request.body)
            print(r.text)


if __name__ == '__main__':
    app = PostFile('13049499944', '123456')
    app.upload_img()
    # app.get_bookshelf_book()
    # app.del_bookshelf_book('APP UI自动化测试专用_ePub')