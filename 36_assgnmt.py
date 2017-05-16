"""
36.l=[1,2,3,[4,5,6],7,[8,9,10]] for single dimentional list
"""

l=[1,2,3,[4,5,6],7,[8,9,10]]
k=[]
for i in l:
    
    if type(i) is list:
        
        for j in i:
            
            k.append(j)
    else:
        k.append(i)

print "Actual Multi dimensional list is ",l
print "Single dimensional list is",k

