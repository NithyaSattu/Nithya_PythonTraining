"""
12. take a string from the user and check contains atleast one alphabets or not?
"""
s=raw_input("enter the string to check whether is has one alphabet or not")

for i in s:
    if i.isalpha():
        print "ture:string has atleast one alphabet"
        break
else:
    print "false:string has no alphabets"
