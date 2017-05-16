import assgnmt70dboperations

obj1=assgnmt70dboperations.database()
con,cur=obj1.connect()
obj1.db_create_op(cur)
obj1.db_insert_op(1,'nithya','nithya@gmail.com',cur,con)
obj1.db_update_op(1,'abc',cur,con)
obj1.db_delete_op(1,cur,con)





