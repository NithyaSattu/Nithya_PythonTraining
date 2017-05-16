"""
77. Remove duplicates elements of the list without
using built in keywords and temporary list.
"""
def remove_duplicates(list1):
    list1.sort()
    i = len(list1)-1
    
    while i > 0:  
        if list1[i] == list1[i-1]:
            list1.pop(i)
        i = i-1
    return list1

if __name__ == "__main__"    :
    
    t1=input("Enter the elements in the list")
    list1=list(t1)
    print "Removed duplicates from the list and the result is",remove_duplicates(list1)       
        


