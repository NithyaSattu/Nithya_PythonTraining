"""
18. Determine the factors of a number entered  by the user
"""
num=input("Enter the number to find the factors")
x=num+1
print "Factors of the given number are:"
for i in range(1,x):
    if num%i==0:
        print i
        
        
        
        


