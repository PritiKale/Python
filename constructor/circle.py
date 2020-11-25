class Circle:

 def __init__(self): # no parameter
  self.r=4

 def area(self):
  c=3.14 * self.r * self.r
  print("Area is: ",c)

 def circum(self):
  c= 2 * 3.14 * self.r
  print("Circumferance is: ",c)

c=Circle()
 # when obj is created progm control call/jump on non
 # paramertrize constuctor & value initialize.
c.area()
c.circum()