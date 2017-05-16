"""
31.Taake numbers from the user and findout min, maximum, sum, average
"""

num=input("enter the numbers separated by comma")
a=0
sum_of_num=0
for i in num:
      
    sum_of_num=sum_of_num+i
    if a<i:
        a=i
    
print "Sum of given %d numbers is" %len(num),sum_of_num
avg=sum_of_num/(len(num))
print "Average of the given numbers is ",avg
print "Maximum value of given numbers is ",a
print "Minimum value of given numbers is ",min(num)

