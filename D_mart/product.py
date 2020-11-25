import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="dmart_py_db")

mycursor=myconn.cursor()

sql="insert into product(pname,rate,qty)values(%s,%s,%s) ";
val=[("pd",500,3),
	  ("table",3000,20),
	  ("chair",3000,10),
	  ("pen",10,100),
	  ("laptop",30000,3)
	];

mycursor.executemany(sql,val);
myconn.commit();
print("Recorde inserted successfully");

