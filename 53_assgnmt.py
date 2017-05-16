"""
53. Sort the list marks = [("mohan", 80), ("satish", 90), ("purnesh", 40),
("venkat", 30)]
acording to descending order of marks

"""

marks = [("mohan", 20), ("satish", 40), ("purnesh", 5),("venkat", 10),("jhon",66)]
list1=[]
while marks:
    val_t=marks[0]
    val_s=marks[0][1]
    for i in marks:
              
        if i[1] > val_s:
            val_t=i
            val_s=i[1]
    list1.append(val_t)
    marks.remove(val_t)
    
    
print "Descending order of the marks in the given list",list1
        
