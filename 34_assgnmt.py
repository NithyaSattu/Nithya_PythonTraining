"""
34.Convert n dimentional list to single dimentiona list
"""

def sample1(list3):
       
    for i in list3:
    
        if type(i) is list:
            sample1(i)
                 
        else:
            list2.append(i)
if __name__ == "__main__":
    list1=[10,20,30,[40,50,[60,[3,[3,4,5,6,7]]]],70,[80,[90,54,[321,43,21,22],678,98],20]]
    list2=[]
    for x in list1:
        if type(x) is list:
            sample1(x)
        else:
            list2.append(x)
    print "Actual n dimensional list is ",list1
    print "Converted single dimensional list is ",list2
  


