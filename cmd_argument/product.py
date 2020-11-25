import sys

pname=sys.argv[1]
rate=int( sys.argv[2])
qty=int (sys.argv[3])
gst=int (sys.argv[4])

print("Product name is: ",pname)
print("Rate name is: ",rate)
print("Qty is: ",qty)
print("GST is: ",gst)


bill=rate * qty 
gst_amt=(bill*gst)/100
total_amt=gst_amt+bill

print("Total Bill is: ",bill)
print("Gst is: ",gst_amt)
print("Total amount is: ",total_amt)
