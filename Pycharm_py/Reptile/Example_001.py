#coding:utf-8
'''
学会对所要完成的任务进行步骤分析，然后一步步分解任务，能自行写的代码自己解决，可以借助google搜素去找现成的代码，最后写代码解决问题
如下载PDF文件，需要以下步骤：
1、怎么去请求网络
2、解析网页的内容或标签
3、下载文件
确定请求网络下载网页用requests，解析html用BeautifulSoup，提取下载链接BeautifulSoup，下载文档（stackoverflow中找到了一段下载文件的代码）。
'''

#file-name: download pdf file
import requests
from bs4 import BeautifulSoup

def downloadr_file(url,index):
    local_filename = index+ '-'+url.split('/')[-1]
    #Note ethe stream = True paremeter
    r = requests.get(url,stream=True)
    with open(local_filename,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:#filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

#http://ww0.java4.datastructures.net/handouts/
root_link="http://www.bookresource.net/"
r = requests.get(root_link)
if r.status_code==200:
    soup=BeautifulSoup(r.text)
    #print(soup.prettify(r.text))
    index = 1
    for link in soup.find_all("a"):
        new_link = root_link+link.get('href')
        if new_link.endswith(".pdf"):
            file_path=downloadr_file(new_link,str(index))
            print("downloading:"+new_link+"---->"+file_path)
            index+=1
    print("all download finished")
else:
    print("errors occur")
