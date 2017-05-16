"""
73. addition, substraction, multiplication operations are not
supported by dictionary. Write a program to provide addition,
substraction, and  multiplication operations to dictionary.
Write your own definition for operations.
"""

class Dict_op(dict):
    def __init__(self,obj):
        self.obj = super(Dict_op,self).__init__(obj)
        return self.obj
        
    def __add__(dict1,dict2):
        d3={}
        for i in dict1.keys():
            d3.update({i:dict1[i]+dict2[i]})
        return d3
    def __sub__(dict1,dict2):
        d3={}
        for i in dict1.keys():
            d3.update({i:dict1[i]-dict2[i]})
        return d3
    def __mul__(dict1,dict2):
        d3={}
        for i in dict1.keys():
            d3.update({i:dict1[i]*dict2[i]})
        return d3

if __name__=="__main__":
    
    obj1= Dict_op({"k1":6,"k2":8})
    obj2=Dict_op({"k1":3,"k2":9})
    o1= obj1+obj2
    o2 = obj1-obj2
    o3 = obj1*obj2
    print "Addition of dicts is",o1
    print "Substraction of dicts is",o2
    print "Multiplication of dicts is",o3
    
    
