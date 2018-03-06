class Person:
    def __init__(self):
        self.name="first"
    def setname(self,name):
        self.name=name
        print(self.name)
    def sayhello(self):
        print "My name is:",self.name
p=Person()
p.setname("Apple")
p.sayhello()
a =Person()
a.sayhello()
