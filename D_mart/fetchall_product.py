import mysql.connector
import decimal

myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="dmart_py_db")

mycursor=myconn.cursor()

sql="select * from product"

mycursor.execute(sql);

myresult=mycursor.fetchall();

for x in myresult:
 print(x);

print("------------------------------------------")


sql="select sum(bill_amt) from product"

mycursor.execute(sql);
myresult=mycursor.fetchone();

print("Total Bill Amount ",str(myresult));

print("------------------------------------------")


sql="select sum(bill_amt)*0.40 from product"

mycursor.execute(sql);
myresult=mycursor.fetchone();

print("Discount 40% ",myresult);

print("------------------------------------------")

sql="select sum(bill_amt)-(sum(bill_amt)*0.40) from product"

mycursor.execute(sql);
myresult=mycursor.fetchone();

print("Final Bill",myresult);

