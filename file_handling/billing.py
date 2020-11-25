file=open("billing.txt","w")

Product=input("Product name:")
rate=int(input("Rate :"))
qty=int(input("Quantity: "))


bill=rate * qty


file.write("\n Product name is: ")
file.write(Product)

file.write("\n Rate is: ")
file.write(str(rate))

file.write("\n Quantity is: ")
file.write(str(qty))

file.write("\n Final Bill Amount is: ")
file.write(str(bill))

print("file write successfully")
