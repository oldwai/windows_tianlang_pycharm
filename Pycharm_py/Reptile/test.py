# -*- coding:utf-8 -*-

"""
import urllib2

url = "https://www.baidu.com"
#req = urllib2.urlopen(url)
response = urllib2.urlopen(url)
the_page = response.read()

print the_page

#coding=utf-8
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("https://www.baidu.com")

print html


# -*- coding:utf-8

#第二个
#数据库连接
import MySQLdb
conn =MySQLdb.connect(
    host="172.16.7.55",
    port = 3306,
    user = "reptile",
    passwd = "reptile123456",
    db = "py_reptile",
)

cur = conn.cursor()

cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


cur.close()
conn.commit()
conn.close()
"""

#第三个
#爬取网页上格式为jpeg的图片

import urllib2,urllib
import re
import 

def getHtml(url):
    response = urllib2.urlopen(url);
    the_page = response.read();
    return the_page;

html = getHtml("http://news.ifeng.com/a/20170331/50872250_0.shtml")

def getImg(html):
    reg = r'src="(.+?\.jpeg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for download_img in imglist:
        urllib.urlretrieve(download_img,'%s.jpeg' % x)
        x+=1

getImg(html)

def con_mysql():
    host = "172.16.7.55"
    dbName= "test_reptile"
    user = "reptile"
    passwd= "reptile123456"
    port="3306"

