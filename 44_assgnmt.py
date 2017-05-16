"""
44. l=['1','2','3'] get the sum of the list
"""


l=raw_input("Enter the numbers in a list to get the sum of it")

k=list(l.split(','))
print "Converted List is ",k
h=0
for i in k:
    p=int(i)
    h=h+p
print "Sum of the numbers in the list is ",h
 




