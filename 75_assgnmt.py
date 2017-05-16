"""
75. implement class method and instance method and static method
in a class with an example. Create a instance and call all the methods.
Write down what is class method and instance method and static method.
"""

class Myclass:
    def __init__(self,a):
        
        self.Name = a

    def Instancemethod(self):
        return 'Instance methods have access to the instance variables, through the special self parameter', self.Name

    @classmethod
    def classmethod(cls):
        return 'Class methods receive the class as a parameter', cls

    @staticmethod
    def staticmethod():
        return 'Static methods do not receive the self parameter, and can be called on the class directly'

obj = Myclass('Nithya')
print obj.Instancemethod()
print Myclass.classmethod()
print Myclass.staticmethod()
