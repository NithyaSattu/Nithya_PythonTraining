"""
64. Take employees info (id,name, age, adress, sal, height, weight)
	a. Take id, provide employee information for that id.
	b. find out average salary.
	c. find out which age, address taking the heighest salary 
	d. find out every employee BMI value
	e. Finally find out the Organization overall BMI
"""

def a():
    f1 = open('source_64.txt','r')
    read_lines = f1.readlines()
    id_input = raw_input("Enter the Id of the employee to view his/her details")
    for i in read_lines:
        if i[0] == id_input:
            print i
    f1.close()        
def b():
    f1 = open('source_64.txt','r')
    read_lines = f1.readlines()
    var1 = 0
    for i in read_lines[1:]:
        i = i.strip(",\n")
        i=i.split(",")
        var1 = var1+ int(i[4])
    print "Average salary = ",var1/(len(read_lines)-1)        
def c():
    f1 = open('source_64.txt','r')
    read_lines = f1.readlines()
    j=[]
    for i in read_lines[1:]:
        i = i.split(',')
        j.append(i[4])
    if i[4] == max(j):
        print "\nHighesh salary employee age and place respectively is",i[2],i[3]
          
    
def d():
    f1 = open('source_64.txt','r')
    read_lines = f1.readlines()
    print "BMI of the every employee respectively are"
    for i in read_lines[1:]:
        i = i.split(',')
        denom = (float(i[5])**2)
        bmi = float(int(i[6])/denom)
        print bmi
    
def e():
    f1 = open('source_64.txt','r')
    read_lines = f1.readlines()
    sum1 = 0
    for i in read_lines[1:]:
        i = i.split(',')
        denom = (float(i[5])**2)
        bmi = float(int(i[6])/denom)
        sum1 = sum1+bmi
    print "Overall organisation BMI value is ",sum1
    
  
if __name__ == "__main__":
    f1 = open('source_64.txt','r')
    
    f1.close()
    while True:
        menu=raw_input("Enter your option\n 1.Enter Id to get info\n 2.Avg Sal\n 3.Highest Sal\n 4.BMI Val \n 5.Organization BMI \n 6.Exit \n")
        if menu == "1":
            a()
        if menu == "2":
            b()
        if menu == "3":
            c()
        if menu == "4":
            d()
        if menu == "5":
            e()
        if menu == "6":
            print "Exiting from the program"
            break
    
        
    
    
