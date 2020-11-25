import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="")

mycursor=myconn.cursor()

mycursor.execute("create database barclays")

print("database create successfully");