"""
15. take a string from the user and check
contains atleast one small letter or not?
"""
r=raw_input("enter the string")
for i in r:
    if i.islower():
        print "Atleast one small letter is present in the given string"
        break
else:
    print "No small letters are present"
    
