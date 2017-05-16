"""
54. write a function to get dynamic list for floating
numbers also based on start and end and step parameters
"""



def float_fun(start_list,end_list,step_val):
    list1=[]
    x=0
    for i in range(start_list,end_list,step_val):
        list1.append(i)
    print list1
    for j in list1:
        x=float(j)
        list1.append(x)
    print list1
        


if __name__=="__main__":
    start_list=input("Enter the starting float value of the list")
    end_list=input("Enter the ending value of the list")
    step_val=input("Enter the step value")
    float_fun(start_list,end_list,step_val)
        

    



