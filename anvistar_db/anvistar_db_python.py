import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="anvistar_db_python")

mycursor=myconn.cursor()

mycursor.execute("create table student(rollno int (5),name varchar (10) , tech varchar (10) , fess bigint(10) , duration varchar (15) , gender char (1))")

print("table create successfully");