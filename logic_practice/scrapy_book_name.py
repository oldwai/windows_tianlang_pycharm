# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

#coding=utf-8
import requests
import re
import sys
import io
import codecs
import csv

#将列表转换成csv文件,方便查看
def listtocsv(csvname, book_lists, is_need_titile):
    with codecs.open(csvname, 'a', 'utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # 写入书名,简介
        if is_need_titile == 0:
            writer.writerow(["book name", "synopsis"])
        # 写入内容
        writer.writerows(book_lists)


#保存爬取的信息
def savefile(filename,books):
    with codecs.open(filename, 'a', 'utf-8') as f:
        for book in books:
            for detail in book:
                f.write(detail + '\n')

#连接网页
def connecturl(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        proxies = {"http": "http://183.222.102.107:80"}
        r = requests.get(url, headers=kv, proxies=proxies)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print("failed!")

#匹配信息
def findmessage(text,msg):
    books = re.findall(msg, text)
    return books

#由于正则表达式|之后的元组格式为('网址',''),('','书名'),所以我把它转换改为列表[['网址',书名]...]的格式
def tupletolist(books):
    num = 0
    flag = 0
    tempflag = 0
    book_lists = []
    book_list = []
    for book in books:
        book_list.append(book[0])
        book_list.append(book[1])
        book_lists.append(book_list)
        book_list = []
    return book_lists



if __name__ == '__main__':
    #page为页数,可以随意修改它的数值,只要在页数范围内
    page = 0
    # 改变标准输出的默认编码,一开始我做的时候并没有出现编码问题,做了几次后就出现问题,所以改了编码
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    #csv文件保存路径和列表保存路径
    is_need_titile = 0
    filename = "E:\\logic_practice\\books.docx"
    csvname = "E:\\logic_practice\\books.csv"
    #从html匹配简介,由于作者和简介匹配的条件是一样的,于是都匹配出来了
    bookdetails = re.compile(r'<div class="intro">([\s\S]*?)</p></div>')
    #匹配带有点击展开全部的内容,用于删除
    modifymsg = re.compile(r'<a href="([^"]+)" class=')
    #这里是将提取的简介,去除掉换行<p></p>
    definebds = re.compile(r'[^\s<p></p>]+')

    #提取简介,合并成一个完整简介
    middle_detail = ''
    #存储['书名','简介']
    final_detail = []
    #fin_books_details是最终存储书名与简介的列表
    final_books_details = []
    while page < 10:
        url = "https://book.douban.com/tag/互联网?start="+str(20 * page)+"&type=T"
        text = connecturl(url)
        message = r'<a href="([^"]+)" title="([^"]+)"'
        books = findmessage(text, message)
        htmls_and_books = tupletolist(books)
        # 整合豆瓣简介信息
        for html_and_book in htmls_and_books:
            detail_text = connecturl(html_and_book[0])
            msgs = re.findall(bookdetails, detail_text)
            #这里是把全部含有点击展开那写中文的都删除,留下作者和简介
            for msg in msgs:
                find_no_ahref = re.findall(modifymsg, msg)
                if(find_no_ahref):
                    msgs.remove(msg)
            #只有信息msgs不为空,才能提取书名和简介
            if msgs:
                #msg[0]是简介,msg[1]是作者信息
                definemsgs = re.findall(definebds, msgs[0])
                #将简介从列表中提取出来,合成一个完整的简介
                for definemsg in definemsgs:
                    middle_detail = middle_detail + definemsg
                final_detail.append(html_and_book[1])#提取书名,然后存储书名
                final_detail.append(middle_detail)#存储简介,与书名合成一个[书名,简介]
                final_books_details.append(final_detail)#存入[[书名1,简介1],[]书名2,简介2,....[书名n,简介n]]
                middle_detail = ''
                final_detail = []
        savefile(filename, final_books_details)
        listtocsv(csvname, final_books_details, is_need_titile)
        final_books_details = []
        #is_need_titile = 1说明不需要再添加writer.writerow(["book name", "synopsis"])
        is_need_titile = 1
        page += 1
