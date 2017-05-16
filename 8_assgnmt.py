"""
8. take a string from the user and check contains only  capiatl letters or not?

"""
r=raw_input("enter a string")
count=0
for i in r:
    if i.isupper()==False:
        count=count+1
if count==0:
    print "all capitals"
else:
    print "contains other chars"
