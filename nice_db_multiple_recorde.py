import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="nice_db")

mycursor=myconn.cursor()

sql="insert into employee (ename,job,salary	,city,comm)values(%s,%s,%s,%s,%s)"
val=[("TURNER","DEVELOPER",50000,"NASHIK",100),
	  ("ALLEN","SALESMAN",50000,"NASHIK",100),
	  ("ASHOK","TRAINER",50000,"NASHIK",100)
	]

mycursor.executemany(sql,val);

myconn.commit();

print("Recorde inserted successfully");
