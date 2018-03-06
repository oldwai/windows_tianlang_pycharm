# -*- coding:utf-8 -*-
#抓取百度搜索结果页的网站标题信息
import urllib
import re
import sys

def getHtml(url):
    page = urllib.urlopen(url)#打开一个URL地址
    html = page.read() #读取打开的URL上的数据
    return html

def getImg(html):
    reg = r'src="(.+?\.gif)" alt='
    imgre = re.compile(reg)  #将正则表达式编译成正则表达式对象
    imglist = re.findall(imgre,html) #读取html中包含imgre的数据
    #print imglist
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法，直接将远程数据下载到本地，图片通过X依次递增命名
    x=0
    for imgurl in imglist:
        try:
            urllib.urlretrieve(imgurl,'E:\\Reptile_pic\\%s.gif' % x)
        except:
            print("Unexpected error:",sys.exc_info()[0])
        x+=1
        #print("正在下载第 %d图片" % x)
    print("gif图片全部下载完成")
    return imglist


#website = raw_input("输入你要爬取图片的网址：")
html = getHtml("http://qq.yh31.com/")
print getImg(html)