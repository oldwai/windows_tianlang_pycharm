# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


n = int(input("Input a integer:"))
if n >1:
    for i in range(2, n):
        if n % i == 0:
            print('no')
            break
    else:
        print('yes')

result = 'no' if 0 in [n % i for i in range(2,n) ] else 'yes'
print('result:',result)