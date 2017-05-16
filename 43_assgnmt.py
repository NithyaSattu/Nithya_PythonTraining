"""
43. Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]
"""

a=input("Enter the numbers in a list")
p=list(a)

b=[]
for i in p:
    if i not in b:
        b.append(i)
print "Actual List is ",p
print "After removing the Duplicates from the given list",b
