"""
4. take a number from the user and check whether it is prime?
"""

num=input("enter the number")

if num==1:
    print "not prime"
else:
    for i in range(2,num):
        if (num % i)==0:
            print "not prime"
            break
    else:
        print "prime"






       
    
