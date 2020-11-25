import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="nice_db")

mycursor=myconn.cursor()

sql="alter table employee add (email varchar(20))";

mycursor.execute(sql);

print("table alter successfully");


