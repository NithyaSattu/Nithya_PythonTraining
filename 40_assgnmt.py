"""
40.WAP to find union and intersection of lists.
"""

list1=input("Enter the first list")
list2=input("Enter the second list")
list3=list(list1)
list4=list(list2)
list5=[]
for i in list3:
    if i in list4:
        list5.append(i)
print "Intersection of two lists is ",list5
list6=list3+list4
list7=[]
for i in list6:
    if i not in list7:
        list7.append(i)
    
print "Union of lists is",list7
    
    
        



