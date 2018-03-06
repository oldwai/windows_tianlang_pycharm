import os  
import urllib  
import re  
  
          
def cbk(a,b,c):  
    per = 100.0 * a * b / c    
    if per > 100:    
        per = 100  
          
    print '%.2f%%' % per  
  
def setdir(dirname):  
    path="D:/down/newpdf/"+dirname  
    if not os.path.exists(path):  
        os.makedirs(path)  
    os.chdir(path)  
    os.getcwd()  
   
def downpdf(url,file):  
    print url  
    filename,msg=urllib.urlretrieve(url,file,cbk)  
      
def search(line):  
    url='http://cn.bing.com/search?q='+line  
    conn=urllib.urlopen(url)  
    nn=conn.read()  
    if len(nn)==292:  
        return False  
    else:  
        reg='<cite>(.*?)</cite>'  
        articles=re.compile(reg).findall(nn)  
        if len(articles)==0:  
              
            return False  
        else:   
            for url in articles:  
                if url[-4:]=='.pdf':  
                    global sv  
                    sv.write(',full')  
                    link=''  
                    link=link.join(url.split('<strong>'))  
                    alink=''  
                    alink=alink.join(link.split('</strong>'))  
                    print alink  
                    if alink[0:4]!='http':  
                        alink='http://'+alink  
                        print alink  
                    downpdf(alink,line+'.pdf')  
                    return True  
        global sv  
        sv.write(',none')  
        return False  
  
def notExistFile(line):  
    if os.path.exists(line+'.pdf'):  
        global sv  
        sv.write(',exist')  
        return False  
    else:  
        return True  
  
path="E:\\Reptile_download\\pdf"
os.chdir(path)  
  
sv=open('readme.csv','wb')  
articleList=open(path+'vis2000.txt')  
for line in articleList:  
    if line !='\n':  
        if line[0]=='~':  
            print 'setdir'  
            setdir(line[1:-1])  
            sv.close()    
            sv=open(line[1:-1]+' readme.csv','wb')  
            continue  
        else:  
            print line  
            line=line[:-1]  
            sv.write(line)  
            print "search "+line[:-1]  
            if notExistFile(line):  
                search(line)  
            else :  
                print 'exist'  
            sv.write('\n')  
              
sv.close() 