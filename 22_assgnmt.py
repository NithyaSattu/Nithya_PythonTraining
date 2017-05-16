"""
22.Find the sum of all the multiples of 3 or 5 below 1000
"""
num=input("Enter 3 or 5 to find the sum of the multiples")
g=num+1
sum_num=0
print "Multiples of given number are:"
for i in range(1,g):
    if num%i==0:
        print i
        sum_num=sum_num+i
print "Sum of the multiples of the given number is ",sum_num
    
        


