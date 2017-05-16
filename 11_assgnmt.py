"""
11. take a string from the user and check contains atleast one digit or not?
"""
g=raw_input("enter a string")
for i in g:
    if i.isdigit():
        print "True :string contains atleast one number"
        break
else:
    print "False:no digits"
