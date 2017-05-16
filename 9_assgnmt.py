"""
9. take a string from the user and check contains only  small letters or not?
"""

f=raw_input("enter a string")
count=0
for i in f:
     if i.islower()==False:
        count=count+1
if count==0:
    print "contains only small letters"
else:
    print "contains other chars"
        
        
    
    
