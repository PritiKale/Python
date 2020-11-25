import biling;

bamt=biling.bill()

 if(bamt>=10000):
  dis=bamt*0.30
  fbill=bamt-dis
  print("Bill amount is: ",bamt)
  print("Discount amount is 30%: ",dis)
  print("Final bill amount is: ",fbill)