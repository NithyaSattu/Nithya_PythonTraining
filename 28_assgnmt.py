"""
28. WAP> 10 -> 000010
       100 ->  000100
      1000 ->  001000
  2345678  ->  2345678

"""

t1=raw_input('Enter the numbers')
list1=t1.split(',')
print list1
max_list1=max(list1)
k=len(max_list1)
for i in list1:
    
    print str(i).zfill(k)
    

