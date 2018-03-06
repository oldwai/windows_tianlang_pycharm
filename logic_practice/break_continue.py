# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

#题目：计算小于100的最大素数

#负数步长，从最大的
# for n in range(100, 1, -1):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         #为素数
#         print(n)
#         break
import random



#url = "http://testlink.mprtimes.net/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
import string

str1 = string.ascii_letters
str2 = string.digits
test = random.choice(string.ascii_letters + string.digits)
print(str1,str2,test,end='\n')