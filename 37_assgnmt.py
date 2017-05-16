"""
37.l=['a','A','b','B','d','D','c','C'] WAP to find
out case insensitive count and case insensitive search for an element.
"""

l=raw_input("Enter the chars separated by comma")

y=l.lower()
x=raw_input('Enter the char to search and count')
converted_x=x.lower()

for i in l:
    if l.find(x)!=-1:
        v=y.count(converted_x)
    
    else:
        print "char not found"
        break
        
print "count of entered char %s is " %x,v
