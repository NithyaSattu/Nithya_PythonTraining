"""
58. WAP to remove n occurances of specified element from a list
"""


k=input("Enter the numbers in a list")
list1=list(k)
number1=input("enter the number to remove")
oc=input("enter the number of occurances of a number to remove")

for i in range(oc):
    list1.remove(number1)
print "Modified list is",list1
        
        

