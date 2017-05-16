"""
45. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists
"""

l1=[1,2,3,4]
l2=[5,6,7,8]
zip_list=zip(l1,l2)
sum_list=[]
#print zip_list
for i in zip_list:
    m=i[0]+i[1]
    sum_list.append(m)
    
print "List of sum of given lists is",sum_list
