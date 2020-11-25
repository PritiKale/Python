import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="nice_db")

mycursor=myconn.cursor()

sql="select ename,job,salary,salary*12 package from employee"

mycursor.execute(sql);

myresult=mycursor.fetchall();

for x in myresult:
 print(x);
