"""
24. Write a program to findout biggest number in the given numbers.
"""
k=input("Enter the numbers separated by comma:")
print "Entered numbers are ",k
x=0
for i in k:
    if i>x:
        x=i
print "Biggest number from the given numbers is ",x
        
    
