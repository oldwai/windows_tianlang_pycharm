# -*- coding:utf-8 -*-  
# __auth__ = mocobk

import requests
import json
import xlrd
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class GetPreCode:
    def __init__(self, host1, host2, port, account1, passwd1, account2, passwd2,
                 bookname, pinyin, book_auth, is_download):
        self.s = requests.Session()

        self.host1 = host1
        self.host2 = host2
        self.port = '' if port == '80' else port
        self.account1 = account1
        self.passwd1 = passwd1
        self.account2 = account2
        self.passwd2 = passwd2
        self.bookname = bookname
        self.pinyin = pinyin
        self.book_auth = book_auth
        self.is_download = is_download
        # requests库请求HTTPS时,因为忽略证书验证,会有警告，这里禁止警告
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # 申请前置码
    def apply_pre_code(self):
        # 登录
        payload = {'accountId': self.account1, 'password': self.passwd1,
                   'validCode': '1111'}
        root_url = 'https://' + self.host1 + ':' + self.port
        self.s.get(
                root_url + '/mpr/portal-mcrs-publisher/mvc/publisher/login.json',
                params=payload, verify=False)
        r = self.s.get(
                root_url + '/mpr/portal-mcrs-publisher/mvc/publisher/login.json',
                params=payload, verify=False)
        return_dict = re.findall('{.+}', r.text)[0]
        # print(return_dict)
        publisher_name = json.loads(return_dict)['userinfo'][
            'publisherCn']  # 获取出版社名称
        publisher_id = json.loads(return_dict)['userinfo'][
            'publisherId']  # 获取出版社id
        # print(publisher_name,publisher_id)
        # 申请前置码
        post_data = (('specifyPublisherType', '0'),
                     ('infoIntegrity', '2'),
                     ('bookNameCn', self.bookname),
                     ('bookNamePinyin', self.pinyin),
                     ('productType', 'BA'),  # 产品形式
                     ('bookmaker', publisher_name),
                     ('tempclcId', '199'),  # 中图分类法 1 （工业技术）
                     ('clcId', '199!-!211'),  # 中图分类法 2 （自动化技术、计算机技术）
                     ('langId', 'chi'),
                     ('publishCountry', 'CN'),
                     ('pages', '200'),
                     ('wordage', '2000'),
                     ('colors', '1'),
                     # ('priceType', 'CNY'),
                     ('specifyPublisherName', publisher_name),
                     ('editing', self.book_auth),
                     ('isbn', '978'),
                     ('isbn', '1'),
                     ('isbn', '1212'),
                     ('isbn', '1212'),
                     ('isbn', '1'),
                     ('specifyPublisherId', publisher_id),
                     ('author', self.book_auth),
                     ('codeType', '1'))
        r = self.s.post(
                root_url + '/mpr/portal-mcrs-perecode/mvc/bookportal/addPrefixCodeByPublication.json',
                data=post_data)
        if r.text == '1':
            print('图书《%s》审请前置码成功！' % self.bookname)
        else:
            print('图书《%s》审请前置码失败！' % self.bookname)

    # 审核前置码
    def verify_pre_code(self):
        # 登录
        payload = {'userName': self.account2, 'passWord': self.passwd2,
                   'codeCon': '1111'}
        root_url = 'https://' + self.host2 + ':' + self.port
        self.s.get(root_url + '/mpr/mcrs-system/mvc/syslogin/syslogin.json',
                   params=payload, verify=False)
        # 查询图书并获取图书的id
        post_data1 = (('page', '1'),
                      ('rows', '10'),
                      ('portalOrBackground', 'background'),
                      ('statusScope', 'apply'),
                      ('codeType', '1'),
                      ('bookNameCn', self.bookname))

        r = self.s.post(
                root_url + '/mpr/mcrs-perecode/mvc/bookmanager/queryBook.json',
                data=post_data1)
        # print(json.loads(r.text))
        book_id = json.loads(r.text)['data'][0]['bookId']
        # 审核通过图书
        post_data2 = {'publicationId': book_id, 'codeType': '1'}
        r = self.s.post(
                root_url + '/mpr/mcrs-perecode/mvc/bookmanager/approvalBookApplyOK.json',
                data=post_data2)
        if r.text == '1':
            print('图书《%s》审核成功！' % self.bookname)
        else:
            print('图书《%s》审核失败！' % self.bookname)

    # 下载前置码
    def download_pre_code(self):
        root_url = 'https://' + self.host2 + ':' + self.port
        #审核后接口提交数据，审核前portalOrBackground的background改为manager
        #statusScope为空
        post_data = (('page', '1'),
                     ('rows', '10'),
                     ('portalOrBackground', 'manager'),
                     ('statusScope', ''),
                     ('codeType', '1'),
                     ('bookNameCn', self.bookname))
        r = self.s.post(
                root_url + '/mpr/mcrs-perecode/mvc/bookmanager/queryBook.json',
                data=post_data)
        # 授权文件存放路径，可以直接访问链接下载
        fp_path = json.loads(r.text)['data'][0]['serviceFilePath']
        file_name = self.bookname + ".mra"
        print("图书 %s 授权文件下载地址:\n %s" % (self.bookname, fp_path))
        # 下载前置码文件，文件保存在当前目录下
        res = requests.get(fp_path)
        if not res.raise_for_status():
            with open(file_name, 'wb') as f:
                f.write(res.content)


def read_form(data_file):
    wb = xlrd.open_workbook(data_file)
    sheet = wb.sheets()[0]
    host1 = sheet.cell(1, 1).value
    port = sheet.cell(1, 2).value
    account1 = sheet.cell(1, 3).value
    passwd1 = sheet.cell(1, 4).value
    host2 = sheet.cell(2, 1).value
    account2 = sheet.cell(2, 3).value
    passwd2 = sheet.cell(2, 4).value
    bookname = sheet.cell(4, 1).value
    pinyin = sheet.cell(5, 1).value
    book_auth = sheet.cell(6, 1).value
    is_download = sheet.cell(7, 1).value
    return host1, host2, port, account1, passwd1, account2, passwd2, bookname, pinyin, book_auth, is_download


if __name__ == '__main__':
    host1, host2, port, account1, passwd1, account2, passwd2, bookname, pinyin, book_auth, is_download = read_form(
            './data_form.xls')
    get_pre_code = GetPreCode(host1, host2, port, account1, passwd1, account2,

                              passwd2, bookname, pinyin, book_auth, is_download)
    get_pre_code.apply_pre_code()
    get_pre_code.verify_pre_code()
    if is_download == "是":
        get_pre_code.download_pre_code()
    t = input('按回车键结束！')
