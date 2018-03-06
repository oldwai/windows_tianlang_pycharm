#coding:utf-8
'''
@author:oldwai
'''


#-*- coding:utf-8 -*-
import re
import os
#import requests
import urllib.request

import socket
socket.setdefaulttimeout(5)
keyword = ""
i = 0

def dowmloadPic(html, word):
    global i
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    print ('keyword: '+keyword+' downloading...')
    dir = 'pictures\\'+keyword
    if os.path.exists(dir) == False:
        os.makedirs(dir)
    for each in pic_url:
        if each.endswith('.jpg') == False:
            print("not a jpg picture"+each)
            continue
        print ('Downloading index('+str(i+1)+'), url:'+str(each))
        try:
            string = dir+"\\"+word+'_'+str(i) + '.jpg'
            print(string)
            urllib.request.urlretrieve(each, string)
            #pic= requests.get(each, timeout=10)
        except :
            print ('failed to download the current picture')
            continue
        #resolve the problem of encode, make sure that chinese name could be store
        #fp = open(string.decode('utf-8').encode('cp936'),'wb')
        #fp.write(pic.content)
        #fp.close()
        i += 1



if __name__ == '__main__':
    word = input("Input key word: ")
    keyword = word
    word = urllib.parse.quote(word)
    page = 0
    while 1 :
        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&pn='+str(page)+'&ct=&ic=0&lm=-1&width=0&height=0'
        #result = requests.get(url)
        print('download url:'+ url)
        result = urllib.request.urlopen(url).read()
        result = result.decode('utf-8')
        dowmloadPic(result, word)
        page += 20


main()