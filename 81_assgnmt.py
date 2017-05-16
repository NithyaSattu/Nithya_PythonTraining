"""
82.take two lists keys, values and form a dictionary
"""

t1=input("Enter the first list")
t2=input("Enter the second list")
l1=list(t1)
l2=list(t2)
l3=list(zip(l1,l2))
d={}
for i,j in l3:
	if i in d:
		d[i]=d[i]+j
	else:
		d[i]=j
print "Dictionary formed from two lists is",d
