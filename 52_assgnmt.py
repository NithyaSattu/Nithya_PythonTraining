"""
keys=['k1','k2'], values = ['v1','v2'] form a dictionary.
"""

dict1={}
keys1=raw_input("Enter the keys of a dictionary")

values1=raw_input("Enter the values of the dictionary")
k1=list(keys1.split(','))
v1=list(values1.split(','))
j=0
for i in k1:
    
    dict1[i]=v1[j]
    j=j+1
print "Dictionary formed from the given keys and values is",dict1
