"""
38.l=['a','A','b','B','d','D','c','C']  sort the list properly
"""

l=['a','A','b','B','d','D','c','C']
l1=[]
while l:
    min1=l[0]
    for i in l:
        if i<min1:
            min1=i
    l1.append(min1)
    l.remove(min1)
        
    
print "Sorted list is ",l1
    

