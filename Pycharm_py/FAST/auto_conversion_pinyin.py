
#-*-coding:utf-8-*-
from pinyin import PinYin
#module for excel handle
import xlrd
from xlutils.copy import copy

def name_tran(str):
    test=PinYin()
    test.load_word()
    str[0]
    family=test.hanzi2pinyin(string=str[0])[0]
    last=u''
    print (str[1:])
    for word in test.hanzi2pinyin(string=str[1:]):
        last=last+word

    name_en=last.title()+u' '+family.title()
    return name_en


def file_fill(file_name,sheet_name,row_count):
    #打开Excel文件读取数据
    data = xlrd.open_workbook(file_name)
    print type(data)
    #获取一个工作表
    #table = data.sheets()[0]#通过索引顺序获取
    #table = data.sheet_by_name(sheet_name)#通过名称获取
    table = data.sheet_by_index(2) #通过索引顺序获取
    #using xlutils to modify excel
    wb = copy(data)
    #通过get_sheet()获取的sheet，有write()方法
    ws = wb.get_sheet(2)
    for i in range(1,row_count):
        name_cn=table.cell(i,1).value
        print(type(name_cn))
        try:
            name_en=name_tran(name_cn)
            ws.write(i,2,name_en)
            print (name_en)
        except:
            print (i+1,"throw fail to translate.")
    wb.save(file_name)
    return "Over!"

if __name__=="__main__":
    file_fill(u"test.xls",u"test",100)