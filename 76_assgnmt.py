"""
76.  write a class program to demonstrate method overloading in python
using below scenario.
 	Write a class and constructor to create an instances like below
	a. p1 = person(id=1,name=”ashok”,age=23,sal=56787)
            b. p2 = person(id=2,age=24,adhar=23456)
	c. p3 = person(id=4,pan=”brcp3456”,sal=23,age=45)	
make instance iterable and provide the operation sp1+p2, p1-p2.
Give your own definition for the operations
"""

class Person_Methodoverlodng(object):
    def __init__(self,id1=0,name='',age=0,sal=0,pan=0,adhar=0):
        self.id1 = id1
        self.name = name
        self.age = age
        self.sal = sal
        self.pan = pan
        self.adhar = adhar
    def get_info(slef):
        return self.id1,self.name,self.age,self.adhar,self.pan,self.sal
    def __iter__(self):
        yield self.id1
        yield self.name
        yield self.age
        yield self.sal
        yield self.pan
        yield self.adhar
    def __add__(self1,self2):
        res={}
        res.update({'ID':self1.id1+self2.id1})
        res.update({'Name':self1.name+self2.name})
        res.update({'Salary':self1.sal+self2.sal})
        return res

if __name__ == "__main__":
    
    p1 = Person_Methodoverlodng(id1=1,name="ashok",age=23,sal=56787)
    p2 = Person_Methodoverlodng(id1=2,age=24,adhar=23456)
    p3 = Person_Methodoverlodng(id1=4,pan="brcp3456",sal=23,age=45)
    print "Interation trough p1 instance result"
    for i in p1:
        print i
    print "p1+p2 result for ID,Name,Salary",p1+p2

    


        
    
