"""
25.findout third occurance of given substring
"""
str1=raw_input("Enter the string")
sub=raw_input("Enter the substring")
x = 0
y = 0
i = 0

while x<len(str1):
    x=str1.find(sub,x)
    if x != -1 :
        i = i+1
    if x==-1 or i == 4:
        break
    
    x+=1
    y=x

print "3rd occurance of the sub string in the actual string is at index",y-1

    

    
    
    
    
