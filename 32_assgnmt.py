"""
32.l=[10,20,30,[40,50,60],70,[80,90,20]].
Convert this list as sigle dimentiona list
"""
def sample1(list3):
       
    for i in list3:
    
        if type(i) is list:
            sample1(i)
                 
        else:
            list2.append(i)
if __name__ == "__main__":
    list1=[10,20,30,[40,50,60],70,[80,90,20]]
    list2=[]
    for x in list1:
        if type(x) is list:
            sample1(x)
        else:
            list2.append(x)
    print "Actual Multi dimensional list is ",list1
    print "Converted single dimensional list is ",list2
  

