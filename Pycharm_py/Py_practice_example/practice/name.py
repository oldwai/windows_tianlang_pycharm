# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

#练习题1
'''
1、假设要用50、20、10、5、1（元）来找零，给定任意小于100且为整数的找零金额，求最少找零张数

[50,20,10,5,1]
x = input('要找零的钱:---------')
m50 = x // 50
m20 = x%50//20
m10 = x/1000%10
m5 = m/5000%5
m1 = m/25000
if x.isdigit():
    x = int(x)
if x % 50 == 0:
    print('要找%d张零钱'%int(x/50))
if x :
    pass
'''

#练习题2
'''
2、给出一串字符串，求出该字符串中最长的回文字符串
例如：
       给定字符串为 "babad"
	   Output: "bab" or "aba"
'''



#练习题3
'''
3、给定一个由字符串组成的列表，将由相同字符组成的字符串归并在一起
		list = ['ilsi', 'lsii', 'sili',  'isli,  'ilis',  'siil','rmp',
		'prm', 'pmr', 'mrp', 'mpr', 'rpm','kema',  'make','meak', 'mkae',
		 'ekma', 'meka',  'amke', 'kmae', 'test']

		Output:[['isli','lsii'.......],['mpr','pmr'....],['make','ekma'....],['test']]
'''

list01 = ['ilsi', 'lsii', 'sili',  'isli',  'ilis',  'siil','rmp', 'prm',\
          'pmr', 'mrp', 'mpr', 'rpm','kema',  'make','meak', 'mkae',  'ekma', \
          'meka',  'amke', 'kmae', 'test']
iils = []
make = []
mpr = []
test = []
print("原始的列表：",list01)
for i in list01:
    t = "".join((lambda x:(x.sort(),x)[1])(list(i)))
    if t == 'iils':
        iils.append(i)
    elif t == 'mpr':
        mpr.append(i)
    elif t == 'estt':
        test.append(i)
    elif t == 'aekm':
        make.append(i)
    else:
        print("不满足条件")

print("排序之后的列表",list((iils,make,mpr,test)))
input()
