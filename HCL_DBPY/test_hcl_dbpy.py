import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="")

mycursor=myconn.cursor()

mycursor.execute("create database HCL44_DB_PY")

print("Database create successfully");

#code  for creating table 
myconn1=mysql.connector.connect(host="localhost",user="root",passwd="",database="HCL44_DB_PY")
mycursor1=myconn1.cursor()
mycursor1.execute("create table customer (custid int (5), cname varchar(10),city varchar(10), phoneno bigint(10))")
print("Table create successfully");


#code  for inserting recorde
mycursor2=myconn1.cursor()

sql="insert into customer(custid,cname,city,phoneno)values(%s,%s,%s,%s)"
val=(101,"PRITI","DECCAN",7845123256)

mycursor2.execute(sql,val);
myconn1.commit();
print("Recorde inserted successfully");