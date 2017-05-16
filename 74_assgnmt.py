"""
74. write a class that can create only one object.
IF create one more object then it should written existing object but not new.
Create three instances and print id’s of the instances.
All the id’s should show same address.
"""
class Class1(object):
    obj= False
    def __new__(cls,a,b):
        if not cls.obj:
            cls.obj = super(Class1,cls).__new__(cls)
            print "Calling parent class method"
        return cls.obj
    def __init__(self,a,b):
        print "calling init method"
        self.a = a
        self.b = b
    def get(self):
        print "method inside class"
        return self.a,self.b
obj1=Class1(50,1500)
obj2=Class1(100,10)
obj3 =Class1(12,200)
print obj1.get()
print obj2.get()
print obj3.get()

print id(obj1),id(obj2),id(obj3)
