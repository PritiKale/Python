import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=myconn.cursor()
mycursor.execute("create database HCL_DB5_PY")
print("Database create successfully");


#code  for creating table 
myconn1=mysql.connector.connect(host="localhost",user="root",passwd="",database="HCL_DB5_PY")
mycursor1=myconn1.cursor()
mycursor1.execute("create table customer (custid int (5), cname varchar(10),city varchar(10), phoneno bigint(10))")
print("Table create successfully");


#code  for inserting recorde
myconn2=mysql.connector.connect(host="localhost",user="root",passwd="",database="HCL_DB5_PY")
mycursor2=myconn2.cursor()
sql="insert into customer (custid,cname,city,phoneno) values (%s,%s,%s,%s)"
val= (101,'RAM','PUNE',7845123256)
mycursor2.execute(sql,val)

print("Recorde inserted successfully");