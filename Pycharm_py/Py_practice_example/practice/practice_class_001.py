#coding:utf8
'''
类数据属性和实例数据属性，可以总结为：

类数据属性属于类本身，可以通过类名进行访问/修改
类数据属性也可以被类的所有实例访问/修改
在类定义之后，可以通过类名动态添加类数据属性，新增的类属性也被类和所有实例共有
实例数据属性只能通过实例访问
在实例生成后，还可以动态添加实例数据属性，但是这些实例数据属性只属于该实例

类数据属性属于类本身，被所有该类的实例共享；并且，通过实例可以去访问/修改类属性。
'''

# class Student(object):
#     count = 0
#     books = []
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         pass
#         print(self.name,self.age)
#     pass

def foo(bar=[]):        # bar是可选参数，如果没有提供bar的值，则默认为[]，
    bar.append("baz")    # 但是稍后我们会看到这行代码会出现问题。
    return bar

def foo2(x=1,y=2):        # bar是可选参数，如果没有提供bar的值，则默认为[]，
    #bar.append("baz")    # 但是稍后我们会看到这行代码会出现问题。
    return x,y

print foo()
print foo2()