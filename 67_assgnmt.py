"""
67. Collect emp information in a file Provide these operations.
    
    Menu:
     1. Get information of an employee
     2. Modify employee information
     3. delete an employee information (Only status field change in the employee file)
     4. Add an employee.

"""

def get_info():
    f1 = open('source_67_csv.csv','r')
    read_lines = f1.readlines()
    var = raw_input("Enter the id of the emp")
    for i in read_lines[1:]:
        i=i.split(',')
        if i[0] == var:
            print "Details of the emp are",i
    
    f1.close()
def modify_row():
    f1 = open('source_67_csv.csv','r')
    readlines_modify = f1.readlines()
    modify_id = raw_input("Enter the ID which u want to change")
    modify_what = raw_input("Enter which feild u want to change name or age")
    new_value = raw_input("enter new value")
    for i in range(len(readlines_modify)):
        j = readlines_modify[i].split(",")
        print "I",i
        print "J",j
        if j[0] == modify_id:
            if modify_what == "name":
                x = j[2]
                print x
                print i
                del readlines_modify[i]
                readlines_modify.insert(i,modify_id+","+new_value+","+x)
            elif modify_what == "age":
                x=j[1]
                print "X",x
                del readlines_modify[i]
                readlines_modify.insert(i,modify_id+","+x+","+new_value+"\n")
                
    f1.close()
    f1 = open('source_67_csv.csv','w')
    f1.writelines(readlines_modify)                                                                                 
    f1.close()
       
def delete_row():
    f1 = open('source_67_csv.csv','r')
    readlines_modify = f1.readlines()
    modify_id = raw_input("Enter the ID which u want to change")
    modify_what = raw_input("Enter what(status)")
    new_value = raw_input("enter new value")
    for i in range(len(readlines_modify)):
        j = readlines_modify[i].split(",")
        if j[0] == modify_id:
            if modify_what == "Status":
                x= j[1]
                y = j[2]
                del readlines_modify[i]
                readlines_modify.insert(i,modify_id+","+x+","+y+","+new_value+"\n")
            
                
    f1.close()
    f1 = open('source_67_csv.csv','w')
    f1.writelines(readlines_modify)                                                                                 
    f1.close()
def add_emp():
    f1 = open('source_67_csv.csv','r')
    rows =[]
    h=input("Enter the EMP ID")
    f=raw_input("Enter the name")
    g=raw_input("Enter the age")
    row="{0},{1},{2}".format(h,f,g)
    row = row+"\n"
    rows.append(row)
    rows=map(lambda x: x+"\n",rows)
    f1.close()
    f1 = open('source_67_csv.csv','a')
    f1.writelines(rows)
    f1.close()
if __name__ == "__main__":
    f1 = open('source_67_csv.csv','r')
    f1.close()
    while True:
        menu=raw_input("Enter your option\n 1.Display contents\n 2.modify a row\n 3.delete a row\n 4.Add a emp\n 5.Exit\n")
        if menu == "1":
            #display info
            get_info()
           
        if menu == "2":
            #Modify a row
            modify_row()
            
        if menu == "3":
            #delete a row
            delete_row()
        if menu == "4":
            #Add a emp
            add_emp()
            
        if menu == "5":
            #Exit
            print "Exiting from the program"
            break
        
       



