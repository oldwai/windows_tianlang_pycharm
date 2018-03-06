#coding:utf-8
'''
@author:oldwai
'''

def compare_num(num1, num2):
    if num1 > num2:
        print("%s大于%s" % (num1, num2))
    elif num2 > num1:
        print("%s大于%s" % (num2, num1))
    else:
        print("%s等于%s" % (num1, num2))

if __name__=="__main__":
    num1=raw_input("please input first number:")
    num2=raw_input("please input second number:")
    compare_num(num1,num2)

