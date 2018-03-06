# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


import datetime
import glob
import json
import random

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3


class FanmeiApp:
    def __init__(self, account, passwd):
        self.s = requests.Session()

        self.host = 'https://172.16.3.121/'
        self.account = account
        self.passwd = passwd

        # requests库请求HTTPS时,因为忽略证书验证,会有警告，这里禁止警告
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        urllib3.disable_warnings()
        self.user_id = self.login()

    def api_url(self, endpoint):
        """
        接口地址拼接
        :param endpoint:接口path
        :return:
        """
        url = ''.join(self.host, endpoint)
        return url

    def post_response(self, url, **DataAll):
        """
        封装post请求的方法
        DataAll为一个字典，如json=data，files=files，传入的形式为{"json":data,"files":files}
        目前只用到部分参数，如headers和cookie也可以添加传入params
        :param url: 接口的地址
        :param DataAll: 传入的数据封装
        :return: 返回值为json格式，
        """
        params = DataAll.get('params')
        data = DataAll.get('data')
        json = DataAll.get('json')
        files = DataAll.get('files')
        try:
            resp = self.s.post(url, params=params, data=data,
                               json=json, files=files, verify=False)
            resp.encoding = 'utf-8'
            resp = resp.json()
            return resp
        except Exception as e:
            print("Post请求错误：%s" % e)

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

    def book_search(self):
        pass

    def get_bookshelf_goodsid(self, search_name):
        """
        获取加入书架上的书的goods_id，搜索的书名必须要在登录的账号上加入书架才能搜素到
        否则返回为空
        :param search_name: 通过书名关键字查询
        :return: 有结果则返回goods_id，否则没有返回
        """
        post_data = {"page_index": "0",
                     "p_version": "1",
                     "page_size": "120",
                     "user_id": self.user_id}
        post_url = self.host + 'api/bookclubserver/bookreader/fprint/get'
        DataAll = {'json': post_data}
        r = self.post_response(post_url, **DataAll)
        # print(search_name)
        for index in r["status"]:
            book_name = index["name"]
            goods_id = index["goods_id"]
            # print(search_name,book_name,goods_id)
            if search_name in book_name:
                return goods_id
            else:
                continue

    def get_target_id(self, source_content, search_name, is_epub=True,
                      all_target_id=None):
        """
        此函数获得单个ISLI源下名称为"接口自动化添加" 或者 "auto_add"的id号
        :param all_target_id: 所有的ISLI 目标ID号
        :param isli_source_id: isli源ID，通过他查找下面的所有目标
        :return: 返回所有目标的ID
        """

        isli_source_id = self.query_source_id(is_epub)
        real_user_id = self.user_id
        # isli_source_id = "151563926401647000"
        if all_target_id is None:
            all_target_id = []
        post_data = {"p_version": "1",
                     "page_size": "2000",
                     "user_id": self.user_id,
                     "page_index": "0",
                     "isli_source_id": isli_source_id}
        target_list_url = "https://172.16.3.121/api/bookclubserver" \
                          "/isli/versions/targetlist/get"
        DataAll = {'json': post_data}
        r = self.post_response(target_list_url, **DataAll)
        try:
            x = len(r["status"]["versions"][0]["targets"])
        except:
            print("没有数据可删除")
        else:
            for item in range(x):
                target_id = r["status"]["versions"][0]["targets"][item][
                    "target_id"]
                target_user_id = r["status"]["versions"][0]["targets"][item][
                    "user_id"]
                # print(target_id, type(target_content), target_content)
                if real_user_id == target_user_id:
                    all_target_id.append(target_id)
        return all_target_id

    def epub_sources_id(self, search_name, all_isli_sourceid=None):
        '''
        获取epub书所有的isli_source_id和对应的文本内容
        :param all_target_id:
        :return:返回的是一个"isli_sources"包含字典的列表
        '''
        goods_id = self.get_bookshelf_goodsid(search_name)
        if all_isli_sourceid is None:
            all_isli_sourceid = {"isli_sources": []}
        post_data = {"p_version": "1",
                     "user_id": self.user_id,
                     "goods_id": goods_id}
        isli_sources_url = "https://172.16.3.121/api/bookclubserver" \
                           "/isli/source/get/extra"
        DataAll = {'json': post_data}
        r = self.post_response(isli_sources_url, **DataAll)
        if r["return_code"] == "0":
            isli_sources = r["status"]["isli_sources"]
            # 获取本书所有的源和源内容，删除其他无用的返回值
            for dic in isli_sources:
                # 字典推导式筛选值
                isli_sources_dic = {k: v for k, v in dic.items() if (
                    k == "isli_source_id" or k == "source_content")}
                all_isli_sourceid["isli_sources"].append(isli_sources_dic)
            all_isli_sourceid = json.dumps(all_isli_sourceid, indent=4,
                                           sort_keys=True,
                                           ensure_ascii=False)
            #将获取到的isli源写入all_isli_sources.txt，暂时好像没用
            with open('./all_isli_sources.txt', 'wb') as f:
                f.write(all_isli_sourceid.encode())
            finally_all_isli_sourceid = json.loads(all_isli_sourceid)
            return finally_all_isli_sourceid

    def pdf_sources_id(self, goods_id, all_pdf_sourceid=None, page_num="2"):
        """
        获取pdf书所有的pdf_source_id和对应的文本内容
        因pdf电子书无法一次查到所有的源ID，只能通过在某一页查询，目前优化查询所有
        可以使用for 循环赋值给start
        :param goods_id:
        :param all_pdf_sourceid:
        :param page_num: 源所有的页码
        :return: 返回的是一个"pdf_sources"包含字典的列表
        """
        # goods_id = self.get_bookshelf_goodsid(search_name)
        if all_pdf_sourceid is None:
            all_pdf_sourceid = {}
        post_data = {"p_version": "1",
                     "user_id": self.user_id,
                     "page_no_end": page_num,
                     "page_no_start": page_num,
                     "goods_id": goods_id}
        pdf_sources_list_url = "https://172.16.3.121/api/bookclubserver/" \
                               "bookreader/all/islisource/pdf/get"
        DataAll = {'json': post_data}
        # 调用封装的post_response，返回值json格式
        r = self.post_response(pdf_sources_list_url, **DataAll)
        if r["return_code"] == "0":
            pdf_sources = r["status"]
            all_pdf_sourceid = {"pdf_sources": []}
            # 获取本书所有的源和源内容，删除其他无用的返回值
            for dic in pdf_sources:
                # 字典推导式筛选值
                pdf_sources_dic = {k: v for k, v in dic.items() if (
                    k == "source_id" or k == "source_text")}
                all_pdf_sourceid["pdf_sources"].append(pdf_sources_dic)
            all_pdf_sourceid = json.dumps(all_pdf_sourceid, indent=4,
                                          sort_keys=True,
                                          ensure_ascii=False)
            with open('./all_pdf_sources.txt', 'wb') as f:
                f.write(all_pdf_sourceid.encode())
            all_pdf_sourceid = json.loads(all_pdf_sourceid)
            return all_pdf_sourceid

    def from_epub_get_sourceid(self, source_content, search_name):
        """
        通过source_content, search_name获取ISLI 源ID
        :param source_content:
        :param search_name:
        :return:
        """
        goods_id = self.get_bookshelf_goodsid(search_name)
        all_isli_content = self.epub_sources_id(goods_id)["isli_sources"]
        for dict_source in all_isli_content:
            isli_sources_dic = {k: v for k, v in dict_source.items() if (
                source_content in v)}
            if isli_sources_dic:
                return dict_source["isli_source_id"]

    def from_pdf_get_sourceid(self, source_content, search_name):
        """
        通过source_content, search_name获取ISLI 源ID
        :param source_content:
        :param search_name:
        :return:
        """
        goods_id = self.get_bookshelf_goodsid(search_name)
        all_pdf_content = self.pdf_sources_id(goods_id)["pdf_sources"]
        for dict_source in all_pdf_content:
            isli_sources_dic = {k: v for k, v in dict_source.items() if (
                source_content in v)}
            if isli_sources_dic:
                return dict_source["source_id"]


    def add_text_target(self, text, source_content=None,
                        search_name=None, is_epub=True):
        """
        #想把上传图片和text、视频、音频都放在一个函数里，目前不知道该如何做，待定
        添加文本目标，通过is_epub确定是epub还是pdf，然后再去查找source_id，也就是源ID
        :param text:
        :param source_content:
        :param search_name:
        :param is_epub:
        :return:
        """

        goods_id = self.get_bookshelf_goodsid(search_name)
        source_id = self.query_source_id(is_epub)
        post_data = {"p_version": "1",
                     "local_time": "0",
                     "user_id": self.user_id,
                     "isli_source_id": source_id,
                     "text_content": text,
                     # "image_name": ".png",
                     "goods_id": goods_id}
        #想把上传图片和text、视频、音频都放在一个函数里，目前不知道该如何做，待定
        image_url = self.host + 'api/bookclubserver/isli/image/put'
        voice_url = self.host + 'api/bookclubserver/isli/voice/put'
        text_url = self.host + 'api/bookclubserver/isli/text/put'
        files = {'file': open('D:\\screenshot.png', 'rb')}
        DataAll = {'json': post_data}
        # 调用封装的post_response，返回值json格式
        r = self.post_response(text_url, **DataAll)
        if r['return_code'] == '0':
            print("添加文本成功，文本内容为----%s" % post_data["text_content"])
        else:
            print(r['status'])

    def query_source_id(self, is_epub):
        """
        epub和pdf查询源ID的函数不一样
        :param is_epub:
        :return:
        """
        if is_epub:
            source_id = self.from_epub_get_sourceid(source_content, search_name)
        else:
            source_id = self.from_pdf_get_sourceid(source_content, search_name)
        return source_id

    def del_target(self, source_content, search_name, is_epub=True):
        """
        :param source_content: 通过ISLI源的内容，可以找到该源的ID
        :param search_name: 查找的书名，获取书的goods_ID
        :return:
        """
        # 获取改源下所有的ISLI目标的ID
        all_target_id = self.get_target_id(source_content, search_name, is_epub)
        del_target_url = self.host + "api/bookclubserver/isli/target/del"
        user_id = self.user_id
        if all_target_id:
            for i in all_target_id:
                post_data = {"p_version": "1",
                             "user_id": user_id,
                             "isli_id": i}
                DataAll = {'json': post_data}
                # 调用封装的post_response，返回值json格式
                self.post_response(del_target_url, **DataAll)
            print("删除完毕--------------")
        else:
            print("没有数据可删除")

    def chosePic(self, number):
        '''
        随机调取图片
        '''
        pic_list = glob.glob('D:\\upload_pic\\*.jpg')
        up_pic = random.sample(pic_list, number)
        return up_pic

    def upload_img(self, source_content, search_name, is_epub=True):
        goods_id = self.get_bookshelf_goodsid(search_name)
        # isli_source_id = self.from_epub_get_sourceid(source_content,
        #                                            search_name)
        isli_source_id = self.query_source_id(is_epub)
        upload_url = 'https://172.16.3.121/api/bookclubserver/isli/image/put'
        param = {'p_version': '1',
                 'goods_id': goods_id,
                 'local_time': '0',
                 'user_id': self.user_id,
                 'isli_source_id': isli_source_id,
                 'image_name': '.png'}
        param_json = json.dumps(param)
        payload = {'param_json': param_json}
        #随机选择图片文件上传
        pic_path = random.sample(random_pic(), 1)[0]
        # files = {'file': open('D:\\upload_pic\\IMG_3041.jpg', 'rb')}
        files = {'file': open(pic_path, 'rb')}
        r = self.s.post(url=upload_url, data=payload, files=files, verify=False)
        r = r.json()
        if r["return_code"] == "0":
            print("___上传图片成功")
        else:
            print(r)

    def upload_video(self, source_content, search_name):
        """
        上传音频文件，好像上传之后播放不了，不确定是不是限制了音频文件的格式，需要和泛媒后台确认
        :param source_content:
        :param search_name:
        :return:
        """
        goods_id = self.get_bookshelf_goodsid(search_name)
        isli_source_id = self.from_epub_get_sourceid(source_content,
                                                     search_name)
        upload_url = 'https://172.16.3.121/api/bookclubserver/isli/voice/put'
        param = {'p_version': '1',
                 'goods_id': goods_id,
                 'local_time': '0',
                 'user_id': self.user_id,
                 'isli_source_id': isli_source_id,
                 'postfix': '.wav',
                 'voice_duration': '36'}
        param_json = json.dumps(param)
        payload = {'param_json': param_json}
        files = {'file': open('D:\\upload_pic\\00103.wav', 'rb')}

        DataAll = {'data': payload, 'files': files}
        # 调用封装的post_response，返回值json格式
        r = self.post_response(upload_url, **DataAll)
        if r["return_code"] == "0":
            print("___上传音频成功")
        else:
            print(r.text)


def is_substring(substrlist, str):
    '''''
    #判断字符串str是否包含序列substrlist中的每一个子字符串
    #>>>substrlist=['F','EMS','txt']
    #>>>str='F06925EMS91.txt'
    #>>>is_substring(substrlist,str)#return True (or False)
    '''
    flag = True
    for substr in substrlist:  # （就是它可以检查多种文件格式）
        if not (substr in str):  # （这么简单就判断完了，真是厉害呀）
            flag = False

    return flag


def random_pic(findpath="D:\\upload_pic", flagstr=[".JPG"]):
    """
    设置随机调用图片
    :param findpath: 图片文件存放路径
    :param flagstr: 上传文件的类型，不填默认保存所有类型
    :return:
    """
    import os
    filelist = []
    filenames = os.listdir(findpath)
    if (len(filenames) > 0):
        for fn in filenames:
            if (len(flagstr) > 0):
                # 调用函数is_substring，返回指定类型的文件名
                if (is_substring(flagstr, fn)):
                    fullfilename = os.path.join(findpath, fn)  # （路径，文件名）
                    filelist.append(fullfilename)
            else:
                # 默认直接返回所有文件名
                fullfilename = os.path.join(findpath, fn)
                filelist.append(fullfilename)

    # 对文件名排序
    if (len(filelist) > 0):
        filelist.sort()  # （排序）

    return filelist


if __name__ == "__main__":
    # 城市猎人综合测试epub的goods_id
    # account = "13049499944"  #测试名称测试名称
    account = "13000000001"
    passwd = "123456"

    # search_name表示查找的书名
    search_name = "城市猎人"  # goods_id=201801041052512454
    source_content = "安装预编译"
    text = "接口自动化添加--(源)%s" % source_content
    panmedie_reader = FanmeiApp(account, passwd)
    # panmedie_reader.get_bookshelf_goodsid(search_name)
    # 注意，PDF只能加载当前页的source_id，所以记得确定好ISLI源在哪一页
    # 并在pdf_sources_id函数定义page_num
    # panmedie_reader.upload_img(source_content,search_name,is_epub=False)
    # 上传图片
    # for i in range(1000,10000):
    #     print("第 {0}次".format(i))
    #     panmedie_reader.upload_img(source_content,search_name,is_epub=False)
    #     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     isli_text = "00000%d" % i + text + str(current_time)
    #     print("这是第 %d 次输入内容，输入的值为 %s" % (i, isli_text))
    #     panmedie_reader.add_text_target(isli_text,
    #                                     source_content=source_content,
    #                                     search_name=search_name,
    #                                     is_epub=False)
    # 删除源
    # for i in range(1,8):
    #     panmedie_reader.del_target(source_content,search_name,is_epub=False)
    #panmedie_reader.upload_img(source_content, search_name, is_epub=False)
    panmedie_reader.post_response()