# -*- coding:utf-8 -*-
"""
@author:oldwai
"""
# email: frankandrew@163.com

import read_config
import requests
from log import MyLog as Log

localread_config = read_config.ReadConfig()


class ConfigHttp:

    def __init__(self):
        global host, port, timeout
        host = localread_config.get_http("baseurl")
        port = localread_config.get_http("port")
        timeout = localread_config.get_http("timeout")
        self.log =Log.get_log()
        self.logger = self.log.get_logge()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        """

        :return:
        """
        try:
            response = requests.get(self.url, params=self.params,
                                    headers=self.headers,
                                    timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        """

        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers,
                                     data=self.data, files=self.files,
                                     timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


if __name__ =="__main__":
    url='http://api.shein.com/v2/member/login'
    header={'content-type': 'application/x-www-form-urlencoded'}
    data={'email': '123456@163.com','password': '123456'}
    timeout=0.5
    requests.post(url, headers=header, data=data, timeout=timeout)