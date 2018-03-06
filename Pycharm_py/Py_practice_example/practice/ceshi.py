#coding:utf8

'''
age = 22
counter = 0
for i in range(10):
    print ("-->counter",counter)
    if counter<3:
        while True:
            try:
                guess_num = raw_input("请输入一个整数：")
                guess_num = int(guess_num)
                break
            except ValueError,msg:
                print ("你输入的不是整数，请重新输入：")
        if guess_num == age:
            print ("Congratulations! you got it.")
            break
        elif guess_num > age:
             print ("太大!")
        else:
             print ("太小")
    else:
        continue_confirm = raw_input("Do you want to continue because you are wrong")
        if continue_confirm =="y":
                counter = 0
        else:
            print ("byebye")
            break
    counter +=1
'''

def add():
    x,y=1,1
    z = x+y
    return z


func=add
print "函数复制,func=add",func()

call_func=add()

print "调用函数,call_func=add()",call_func