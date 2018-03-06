# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


# import xlrd
#
# data = xlrd.open_workbook("./addNewUser_case.xls")
# #获取工作表，sheet
# table=data.sheet_by_index(0)
# #总行数和列数
# num_rows=table.nrows
# num_col=table.ncols
# #获取行列表的数据
# # print (table.row_values(0))
# #
# # print (table.name,table.nrows,table.ncols)
#
# #先打印执行结果，在修改执行结果
# #print (table.cell(0,0).value)
# column_name=table.row_values(0)
# for i in range(len(column_name)):
#     print(column_name[i])
#     if column_name[i]=="执行结果":
#         table.put_cell(rowx=i,colx=1,ctype=1,value='成功',xf_index=0)
#
# #table.row_values()
import sys
import locale

print("中文")
