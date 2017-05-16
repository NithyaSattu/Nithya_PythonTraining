"""
46. Find third max value of element
in a list with sorting and without sorting a list.
"""

def max_witoutsorting(b):
    c=[]
    for i in b:
        if i not in c:
            c.append(i)
    print "Third biggest values without using sorting is",c[-3]

def max_withsorting(b):
    b.sort()
    c=[]
    for i in b:
        if i not in c:
            c.append(i)
    print "Third biggest values with using sorting is",c[-3]
            

if __name__=="__main__"    :
    a=input("Enter the numbers in a list")
    b=list(a)
    print "Entered list of numbers is ",b
    max_withsorting(b)    
    max_witoutsorting(b)
    
    
    

