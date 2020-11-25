import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="nice_db")

mycursor=myconn.cursor()

sql="select * from employee"

mycursor.execute(sql);

myresult=mycursor.fetchone();
print(myresult);
