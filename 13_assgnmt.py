"""
13. take a string from the user and check contains atleast one chars or not?
"""
str1=raw_input("Enter the string to check it contains atleast one char or not ")
for i in str1:
    if i.isdigit()==False:
        print "String has charcters"
        break
else:
    print "string has no characters in it"
   
    


