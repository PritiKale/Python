import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="barclays_pdb")

mycursor=myconn.cursor()

mycursor.execute("create table customer (cid int(5),name varchar(10))")

print("table created successfully");