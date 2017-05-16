"""
71. write a program to do registration.
     Write a methods in a class DB to open database connection and
     insert details in to database table. 
Write a Model parent class and implement a create method.
Call a database insert method into the create  method.
Write child class person for Model and override method create
method and call the parent(Model) class create method in the child(person) 
create an instance of person class and call the create method.
"""
import sqlite3
class DB(object):
    
    def open_db(self,db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        print "Connected"
        return self.con
        
    @staticmethod
    def insert_data(con,name,age,sal):
        a=(name,age,sal)
        con.execute("insert into Emp1 values(?,?,?)",a)
        con.commit()

class Model(DB):

    def create_table(self,db_name,name,age,sal):
        con=self.open_db(db_name)
        table_create="create table Emp1(name varchar,age INT,sal INT )" 
        con.execute(table_create)
        print "table created"
        DB.insert_data(con,name,age,sal)
        print "inserted data sucesfully"

class Person(Model):
    
    def create(self):
        def creat_table(self,db_name,name,age,sal):
            super(cls,self).create_table(db_name,name,age,sal)



obj=Person()
obj.create_table("JP","jhon","58",1000)
    
        
    
    
