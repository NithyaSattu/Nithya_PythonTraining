"""
60. Show the below menu to the user:
     1. Add a row
     2. modify a row
     3. delete a row
     Go with one unique field in the file. And maintain that unique
     constraint in all file modifiction operations
     Use .CSV file for this program
"""
import random

def add_row():
    f1 = open('source_60.csv','a')
    rows =[]
    h=input("Enter the ID")
    f=raw_input("Enter the name")
    g=raw_input("Enter the age")
    row="{0},{1},{2}".format(h,f,g)
    row = row+"\n"
    rows.append(row)
    rows=map(lambda x: x+"\n",rows)
    f1.writelines(rows)
    f1.close()
def modify_row():
    f1 = open('source_60.csv','r')
    readlines_modify = f1.readlines()
    modify_id = raw_input("Enter the ID which u want to change")
    modify_what = raw_input("Enter which feild u want to change name or age")
    new_value = raw_input("enter new value")
    for i in range(len(readlines_modify)):
        j = readlines_modify[i].split(",")
        if j[0] == modify_id:
            if modify_what == "name":
                x = j[2]
                del readlines_modify[i]
                readlines_modify.insert(i,modify_id+","+new_value+","+x)
            elif modify_what == "age":
                x=j[1]
                del readlines_modify[i]
                readlines_modify.insert(i,modify_id+","+x+","+new_value+"\n")
                
    f1.close()
    f1 = open('source_60.csv','w')
    f1.writelines(readlines_modify)                                                                                 
    f1.close()
       
def delete_row():
    f1 = open('source_60.csv','r')
    readlines_delete = f1.readlines()
    modify_id = raw_input("Enter the ID which u want to delete all its info")
    for i in readlines_delete:
        if i[0]==modify_id:
            readlines_delete.remove(i)
            f1.close()
    f1 = open('source_60.csv','w')
    f1.writelines(readlines_delete)
    f1.close()

if __name__ == "__main__":
    f1 = open('source_60.csv','w')
    coulmns=['ID','NAME','AGE']
    rows=[]
    ages=range(23,60)
    for i in range(10):
        row="{0},name{0},{1}".format(i+1,random.choice(ages))
        rows.append(row)
    rows=map(lambda x: x+"\n",rows)
    rows.insert(0,",".join(coulmns)+"\n")
    f1.writelines(rows)
    f1.close()
    while True:
        menu=raw_input("Enter your option\n 1.Add a row\n 2.modify a row\n 3.delete a row\n 4.Exit\n")
        if menu == "1":
            #Add a row
            add_row()
           
        if menu == "2":
            #Modify a row
            modify_row()
            
        if menu == "3":
            #delete a row
            delete_row()
            
        if menu == "4":
            #Exit
            print "Exiting from the program"
            break
        
       



