#coding:utf-8
'''
 打印出如下图案（菱形）
    *
   ***
  *****
 *******
  *****
   ***
    *
 '''

for n in  range(1,5):
    s=2*n-1
    print ' '*(4-(n+1)/2)+'*'*n