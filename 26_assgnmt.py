"""
26. findout nth occurance of given substring
"""
str1=raw_input("Enter the string")
sub=raw_input("Enter the substring")
x=0
while x<len(str1):
    x=str1.find(sub,x)
    if x==-1:
        break
    print "substring occurances are at",x
    
    x+=1
