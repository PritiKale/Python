import sys

pname=sys.argv[1]
rate=sys.argv[2]
qty=sys.argv[3]

print("Product name is: ",pname)
print("Rate is: ",rate)
print("qty is: ",qty)


bill=int(rate) * int(qty)

print("bill is: ",bill) 