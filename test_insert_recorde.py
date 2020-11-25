import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="bajaj_db_py")

mycursor=myconn.cursor()

sal="insert into customer(cname,city)values(%s,%s)"
val=('Priti','Pune')

mycursor.execute(sal,val);

myconn.commit();

print(" Recorde insert successfully");