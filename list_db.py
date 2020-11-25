import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="")

mycursor=myconn.cursor()

mycursor.execute("show databases")

for x in mycursor:
 print(x)