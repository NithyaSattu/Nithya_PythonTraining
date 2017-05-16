"""
79. WAP to remove substring from the given string
without using replace function

"""

str1=raw_input("Enter the string")
sub_str=raw_input("Enter the substring")
d=str1.split(sub_str)
k="".join(d)
print "Actual string is ",str1
print "Removed string is ",k
           
    
    
    
