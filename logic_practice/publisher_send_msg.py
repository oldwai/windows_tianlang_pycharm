# -*- coding:utf-8 -*-
"""
@author:oldwai
"""
# email: frankandrew@163.com

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class PublishSendMsg():
    def __init__(self, token):
        """
        token太长，定义类时传递
        self.rows在接口里获取的rows默认是5，表示当前页数据，可能存在要查找的书籍不在当前页，
        所以可以调大rows，避免查找数媒文件失败，从而不能发送站内消息
        :param token:
        :param content:要发送的消息内容
        :return:
        """
        # 发送消息需要带上请求头，主要是Token，Accept、User-Agent不带上好像也有问题，这里就都添加了
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) QtWebEngine/5.7.1 "
                          "Chrome/49.0.2623.111 Safari/537.36",
            "token": token
        }
        # 表示从多少条数据里去查询
        self.rows = 5
        # type表示publisher消息的类型：接受消息为1，发送消息为2
        self.type = 2
        # shopId表示出版社的ID，秋丽出版社为1402
        self.shopId = 1402
        self.s = requests.Session()
        self.host = 'http://172.16.3.45:11999/'
        self.get_param_url = self.host + 'pos/v1/orders/1402'
        self.send_msg_url = self.host + 'pms/v1/shop/messages/1402'
        self.get_content_id_url = self.host + 'pms/v1/shop/messages'
        self.del_msg_url = self.host + 'pms/v1/shop/messages/1402'
        # requests库请求HTTPS时,因为忽略证书验证,会有警告，这里禁止警告
        # 这个脚本好像不用，因为都是http的，不确定是否有影响，所有都加上了，每个请求都加了verify=False
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def get_send_msg_book(self, orderNo):
        """
        获取要查询的订单号的手机号码
        :param response:get请求查询的响应值
        :param orderNo: 订单号
        :return:
        """
        param = {"currentPage": 1,
                 "rows": self.rows,
                 "orderBy": "create_time",
                 "orderByTyp": "DESC"}
        try:
            response = self.s.get(self.get_param_url, headers=self.headers,
                                  params=param)
        except Exception as e:
            print("get_send_msg_book 函数执行get请求报错了", e)
        else:
            for dic in response.json()["data"]["orders"]:
                id_price = {k: v for k, v in dic.items() if (
                    k in ["buyerId", "buyerContactPhone"])}
                phone_number = id_price["buyerContactPhone"]
                buyerId = id_price["buyerId"]
            return (phone_number, buyerId)

    def send_msg(self, orderNo, content):
        """
        发送站内消息
        :param orderNo:
        :return:
        """
        customerName, customerId = self.get_send_msg_book(orderNo)
        json_send_msg = {"content": content,
                         "customerName": customerName,
                         "customerId": customerId}
        try:
            r = self.s.post(self.send_msg_url, headers=self.headers,
                            json=json_send_msg, verify=False)
        except Exception as e:
            print("send_msg 函数执行post请求报错了", e)
        return r.status_code

    def get_content_id(self, del_msg_content, content_id=None):
        """
        获取要删除的消息的content_id
        :param del_msg_content: 删除的消息内容
        :param content_id: 删除消息需要传递ID，此函数返回content_id列表
        :return:
        """
        if content_id is None:
            content_id = []
        param = {
            'page': 1,
            'rows': 10000,
            'type': self.type,
            'shopId': self.shopId
        }
        try:
            r = self.s.get(self.get_content_id_url, headers=self.headers,
                           params=param, verify=False)
            # print(r.text)
        except Exception as e:
            print("get_content_id 函数执行get请求报错了", e)
        else:
            r = r.json()
            if r['resultCode'] == '00000000':
                for dic in r['data']:
                    # 判断消息内容是否包含删除的字符串
                    # 如果有，获取ID 加入到content_id列表里（部分匹配）
                    if del_msg_content in dic["content"]:
                        content_id.append(dic['id'])
                    # 如果消息内容完全相等，再加入ID，以便del_msg函数删除（相当于完全匹配）
                    if del_msg_content == dic["content"]:
                        content_id.append(dic['id'])
            return content_id

    def del_msg(self, del_msg_content):
        """
        传入del_msg_content，通过get_content_id函数得到要删除消息的ID
        :param del_msg_content:
        :return:
        """
        current_id = self.get_content_id(del_msg_content)
        if current_id:
            for contentIds in current_id:
                param = {
                    'type': self.type,
                    'contentIds': contentIds
                }
                self.s.delete(self.del_msg_url, headers=self.headers,
                              params=param, verify=False)
        else:
            print("没有可删除的消息")


if __name__ == "__main__":
    # 如果token修改或提示未认证，请变更
    token = 'eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjEwLCJhdWQiOiIxNzIuMTYuMy40NSIsInVuaWZpY2F0aW9uSWQiOiIxNDc1OTc3MDc5NDI3MzkyMiIsIm5hbWUiOiLmm7nno4rljY4iLCJpc3MiOiI2NUNGNkQ0NkIzRjQ0RTE0QUFDRDM1REQ2NTIyNUQwNiIsInJlcXVlc3RJcCI6IjE3Mi4xNi4zLjQ1Iiwic2hvcElkIjoiMTQwMiIsInVzZXJUeXBlIjowLCJleHAiOjE1MTgwODgxNjksImlhdCI6MTUxODA1OTM2OSwiZW1haWwiOiJEbHNha2RqZm9pd2VydWRpbzFfYXBlanJmYWtqZGZAMTU4YWRkc2ZkYWxrZWpyLmNvbSIsImp0aSI6IjA2NzA5MzdlNTg1MTQ0NGU4YTliODBiNzU5OTM2MDY4In0.v1RMuR0cKSOVAAvwhEz1fp6RMwTLmvl-GzViWTgnCw4m3lzUY9YpmPiv8G-PhNhaAxQjC7xZ8ybJAZb1wBHArQ'
    # orderNo:删除消息的订单号
    orderNo = '35117126215030953201'
    # content：消息内容
    content = "auto_api"
    test = PublishSendMsg(token)
    # content可用于发送或者删除，建议消息内容不一样，可以加上时间或者数字，如下可批量发送消息内容
    # for i in range(1000,10000):
    #     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     msg_content = "00000%d" % i + content + str(current_time)
    #     print("这是第 %d 次输入内容，输入的值为 %s" % (i, msg_content))
    #     test.send_msg(orderNo,msg_content)

    # 删除消息时会将符合的值一并删除，如需完全匹配请到get_content_id函数处修改判断条件
    a = test.get_content_id(content)
    print(a)
