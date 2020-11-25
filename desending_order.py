import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="nice_db")

mycursor=myconn.cursor()

sql="select * from employee order by salary desc" ;

mycursor.execute(sql);

myresult=mycursor.fetchall();

for x in myresult:
 print(x);


print("--------------------------------------------------")

mycursor=myconn.cursor()

sql="select * from employee order by empid desc" ;

mycursor.execute(sql);

myresult=mycursor.fetchall();

for x in myresult:
 print(x);