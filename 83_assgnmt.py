"""
83. find out intersection, union, difference of two list
without/with using set
"""
def set_function(list3,list4):
    set1=set(list3)
    set2=set(list4)
    
    print "Intersection of 2 lists using set is",set.intersection(set1,set2)
    print "Union of 2 lists using set is",set.union(set1,set2)
    print "Difference of 2 lists using set is",set.difference(set1,set2)

def without_set(list3,list4):
    list5=[]
    for i in list3:
        if i in list4:
            list5.append(i)
    print "\nIntersection os 2 lists without set is",list5
    list6=list3+list4
    list7=[]
    for i in list6:
        if i not in list7:
            list7.append(i)
    print "Union of lists without soritng is",list7
    list8=[]
    for i in list7:
        if i not in list4:
            list8.append(i)
    print "Difference of lists without sorting is",list8
            
if __name__=="__main__":
        
    list1=input("Enter the first list")
    list2=input("Enter the second list")
    list3=list(list1)
    list4=list(list2)
    set_function(list3,list4)
    without_set(list3,list4)
