#coding:utf-8
'''
@author:oldwai
'''

#下面的代码输出什么？


# list = ['a', 'b', 'c', 'd', 'e']
# print list[10:]


#答案在下面
'''
上面的代码输出[]，并且不会导致IndexError错误

跟你想的一样，当取列表元素的时候，如果索引值超过了元素的个数
(例如在上面的列表中，取list[10])将会导致IndexError错误。
但是，取一个列表的切片的时候，如果起始索引超过了元素个数，
将不会引起IndexError错误，仅返回一个空列表。

这一特性将会导致一些非常难于追踪的bug，因为在运行时根本没有错误产生。
'''

def changeme (mylist):
    mylist.append([1,2,3,4])
    print("Values inside the function:", mylist)
    # return

mylist = [10,20,30,40]
print("Values outside the function:", mylist)

changeme(mylist)

print mylist
print("Values outside the function:", mylist)


