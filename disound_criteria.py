pname=(input("Enter the product name : "))
rate=int(input("Enter the rate : "))
qty=int(input("Enter the Quantity : "))

print(" ")

bill=rate*qty
print("Bill Amount is : ",bill)

if(bill>=10000):
 dis=bill * 0.40
 fbill=bill-dis
 print("Discound Amount is 40% :",dis)
 print("Final Bill Amount : ",fbill)

elif(bill>=5000):
 dis=bill * 0.30
 fbill=bill-dis
 print("Discound Amount is 30% :",dis)
 print("Final Bill Amount : ",fbill)

elif(bill>=3000):
 dis=bill * 0.20
 fbill=bill-dis
 print("Discound Amount is 20% :",dis)
 print("Final Bill Amount : ",fbill)

elif(bill>=1000):
 dis=bill * 0.10
 fbill=bill-dis
 print("Discound Amount is 10% :",dis)
 print("Final Bill Amount : ",fbill)

else:
	print("Not eligible for discount")

