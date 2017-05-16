"""
72. create a user defined datatype, and provide functionalities of
addition substraction and multiplication. Create three instances(obj1,obj2,obj3)
and print an output of obj1+obj2+obj3, obj1-obj2-obj3, obj1*obj2*obj3  

"""
class Operations:
    
    def __init__(self,a):
        self.a = a
        
    def __radd__(self,oth):
        
        return self.a + oth
    
    def __rsub__(self,oth):
        return self.a-oth
    
    def __rmul__(self,oth):
        return self.a * oth
    
obj1 =Operations(10)
obj2 = Operations(20)
obj3 =Operations(30)

print "Addition of objects",obj1+obj2+obj3
print "Substraction of objects",obj1-obj2-obj3
print "Multiplication of objects",obj1*obj2*obj3

    
    
