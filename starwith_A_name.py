import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="nice_db")

mycursor=myconn.cursor()

sql="select * from employee where ename like 'A%'"

mycursor.execute(sql);

myresult=mycursor.fetchall();

for x in myresult:
 print(x);
