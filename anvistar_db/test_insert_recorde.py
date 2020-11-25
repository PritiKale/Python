import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="bajaj_db_py")

mycursor=myconn.cursor()

sql="insert into customer(cname,city)values(%s,%s)"
val=('Priti','Pune')

mycursor.execute(sql,val);
myconn.commit();

print(" Recorde insert successfully");