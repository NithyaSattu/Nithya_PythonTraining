"""
80  WAP to remove perticular element from a given list for all occurancers
"""
a=input("Enter the elements to a list")
k=list(a)
print "Actual list",a
for i in k:
    for i in k:
               
        if k.count(i)>1:
            k.remove(i)
            
print "Removed elements list",k
        
    
