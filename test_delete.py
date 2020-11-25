import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="nice_db")

mycursor=myconn.cursor()

sql="delete from employee where ename='ALLEN' ";

mycursor.execute(sql);

print("recorde delete successfully");

print("----------------------------------------------");


mycursor=myconn.cursor()

sql="update employee set city='BOSTAN' where city='mumbai' ";

mycursor.execute(sql);

myconn.commit();

print("recorde update successfully");

