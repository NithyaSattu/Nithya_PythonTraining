"""
14. take a string from the user and check contains atleast one capital letter or not?
"""
d=raw_input("enter the string")
for i in d:
    if i.isupper():
        print "Atleast one capital is present in the given string"
        break
else:
    print "No capitals"
        
