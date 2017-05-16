"""
48. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]

"""

list1=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
print "Given List is ",list1
list2=[]
list3=[]

for i in range(len(list1)):
    
    if i==((len(list1))-1):
        list2.append(list1[i])
        list3.append(list2)
        
        list2=[]
    else:
        if list1[i]+1==list1[i+1]:
            list2.append(list1[i])
        else:
            list2.append(list1[i])
            list3.append(list2)
            
            
            list2=[]
print "Final List is",list3
        
    
    
