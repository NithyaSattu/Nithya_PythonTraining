"""
82. delete more than one key value pair at a time.
"""

k=raw_input("Enter the keys of a dict")
p=raw_input("Enter the values of a dict")
k_split=k.split(',')
p_split=p.split(',')
list1=(zip(k_split,p_split))
print list1
dict1={}
for i,j in list1:
    if i in dict1:
        dict1[i]=dict1[i]+j
    else:
        dict1[i]=j

print dict1
remove_key=raw_input("Enter the elements to be deleted")
op=remove_key.split(',')
for i in op:
    del(dict1[i])
print "Dictionary after removing the given keys is ",dict1
    
