# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

# -*- coding:utf-8 -*-
import glob
import random
import subprocess
import os
import sys
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests

'''

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW


def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         cwd=os.getcwd(), shell=False, startupinfo=globalStartupInfo)
    p.wait()
    re = p.stdout.read().decode()
    return re


curdir = os.getcwd()
# 连接的手机列表
mobiles = []
cmd = [curdir + '/adb/adb.exe', 'devices']
print(cmd)
#mobilelist = runCmd(cmd)
# mobilelist = mobilelist.split('\r\n')[1:]
# # print(mobilelist)
# for x in mobilelist:
#     if x:
#         mobiles.append(x)
# if mobiles:
#     print(mobiles)
# else:
#     print(['no devices\t no devices'])
# # 取第一个手机的序列号
# xuliehao = '';
# if mobiles:
#     # 取第一个手机设备
#     device = mobiles[0].split('\t')
#     xuliehao = device[0]
#     print(device)
#
# # 有手机连接上就截图
# if xuliehao:
#     # 保存到本地电脑的图片路径
#     timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#     jietupath = 'd:/adb_screen-' + timestamp + '.png'
#     sdcardpath = '/sdcard/screenshot-' + timestamp + '.png'
#     if os.path.exists(jietupath):
#         os.remove(jietupath)
#     print('正在截屏.....')
#     jtcmd = curdir + '/adb/adb.exe   -s ' + xuliehao + ' shell /system/bin/screencap -p ' + sdcardpath
#     print(jtcmd)
#     result = runCmd(jtcmd)
#     print('截图成功.....')
#     # print(result)
#     print('移动图片到本地 %s .....' % jietupath)
#     jtcmd = curdir + '/adb/adb.exe  -s  ' + xuliehao + ' pull ' + sdcardpath + ' ' + jietupath
#     # print(jtcmd)
#     result = runCmd(jtcmd)
#     # print(result)
#     # 删除sd图片
#     jtcmd = curdir + '/adb/adb.exe   -s ' + xuliehao + ' shell rm  ' + sdcardpath
#     # print(jtcmd)
#     result = runCmd(jtcmd)
#     print(result)
#     print('it is moved screenshot to pc success.....')
# else:
#     print('no device!')
'''

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
        print(str(r['status']['user_id']))
        return str(r['status']['user_id'])
    def chosePic(number):
        pic_list = glob.glob('D:\\upload_pic\\*.jpg')
        up_pic = random.sample(pic_list, number)
        return up_pic

    def post_image(self):
        param_json = {"isli_source_id": "151563926401647000",
                      "goods_id": "201801041052512454",
                      "user_id": "147079828067557300",
                      "p_version": "1",
                      "image_name": ".jpg",
                      "local_time": '0'}
        param_json = json.dumps(param_json)
        print(type(param_json))
        image_url = "https://172.16.3.121/api/bookclubserver/isli/image/put"
        data_1 = {"file":('1111.jpg', open('D:\\upload_pic\\IMG_3041.jpg', 'rb')),
                  'param_json': (None, param_json),
                  'user_id': (None, "147079828067557300")}

        # r = self.s.post(image_url, files=files, json=post_data, verify=False)
        r = self.s.post(image_url, files=data_1,verify=False)
        r =r.json()
        if r["return_code"] =="0":
            print("___上传图片成功")
        #print(r.request.body)
        else:
            print(r.text)

#测试随机生成中文字符
import random

def test_unicode(val = None):
    if val == None:
        val=[]
    for i in range(100):
        val = random.randint(0x4e00, 0x9fbf)
    return chr(val)

def IsSubString(SubStrList,Str):
    '''''
    #判断字符串Str是否包含序列SubStrList中的每一个子字符串
    #>>>SubStrList=['F','EMS','txt']
    #>>>Str='F06925EMS91.txt'
    #>>>IsSubString(SubStrList,Str)#return True (or False)
    '''
    flag=True
    for substr in SubStrList:  #（就是它可以检查多种文件格式）
        if not(substr in Str):  #（这么简单就判断完了，真是厉害呀）
            flag=False

    return flag

def random_pic(FindPath,FlagStr=[".JPG"]):
    import os
    FileList=[]
    FileNames=os.listdir(FindPath)
    if (len(FileNames)>0):
       for fn in FileNames:
           if (len(FlagStr)>0):
               #返回指定类型的文件名
               if (IsSubString(FlagStr,fn)):
                   fullfilename=os.path.join(FindPath,fn)  #（路径，文件名）
                   FileList.append(fullfilename)
           else:
               #默认直接返回所有文件名
               fullfilename=os.path.join(FindPath,fn)
               FileList.append(fullfilename)

    #对文件名排序
    if (len(FileList)>0):
        FileList.sort()  #（排序）

    return FileList

if __name__ =="__main__":
    # path ="D:\\upload_pic"
    # pic_path = random.sample(random_pic(path),1)
    # print(pic_path)
    import requests
    r = requests.get("https://www.baidu.com")
    print(r.elapsed.total_seconds())