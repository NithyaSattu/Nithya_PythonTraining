"""
2. write a program to chek given substring is there in actual string or not?
(search should be case insensitive)
"""
string = raw_input("enter the main string").lower()
sub_string = raw_input("enter the sub string").lower()
if sub_string in string:
    print "Substring found"
else:
    print "Substring not found"


