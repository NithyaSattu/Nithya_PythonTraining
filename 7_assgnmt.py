"""
7. take a string from the user and check contains only  special chars or not?
"""
string = raw_input("Enter the string")
if not string.isdigit():
    for i in string:
        if i.isalpha():
            print "not all characters are special characters"
            break
    else:
        print "string contains all special characters"
else:
    print"string contains only digits as characters"



