def bill():
 qty=int(input("Enter Qty: "))
 rate=int(input("Enter rate: "))
 billamt=rate*qty

 print("Bill amount is: ",billamt)
 
 if(billamt>=10000):
  dis=billamt*0.30
  fbill=billamt-dis
 
  print("Discount amount is 30%: ",dis)
  print("Final bill amount is: ",fbill)
 else:
  print("Not eligble for Discount")  
 

 