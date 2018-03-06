#coding:utf-8
#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
def main():
    score=raw_input("please input your grade:\n")
    print score
    if score==None:
        print "error"
    elif score<69:
        print "Your grade is %s ,You got a C"%(score)
    elif score<=89:
        print "Your grade is %s ,You got a B"%(score)
    else:
        print "Your grade is %s ,You got a A"%(score)

main()