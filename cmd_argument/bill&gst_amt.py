import sys

pname=sys.argv[1]
rate=int(sys.argv[2])
qty=int(sys.argv[3])
gst_amt=int(sys.argv[4])

print("Product name is: ",pname)
print("Rate is: ",rate)
print("Quantity is: ",qty)
print("GST Amount is: ",gst_amt)

bill=rate*qty
gstamt=bill*(gst_amt/100)
total_amt= bill + gstamt

print("------------------------------")

print("Bill Amount: ",bill)
print("GST Amount: ",gstamt)
print("Bill with GST: ",total_amt)


