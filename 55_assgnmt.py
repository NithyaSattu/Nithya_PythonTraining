"""
55. find out all perfect numbers in given range
"""
a=input("Enter the limit to find out the perfect numbers in the given range")

k=range(1,a+2)
print "Perfect Numbers are"
for i in k:
    sum1=0
    b=[]
    for j in range(1,i):
                  
        if i%j==0:
            b.append(j)
    for l in b:
        sum1=sum1+l
    
    if sum1==i:
        print i,

    


