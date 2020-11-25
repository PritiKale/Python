class Circle:
 r=5

 def displayData(self):
  print("Radius is: ",self.r)

 def area(self):
  a=3.14*self.r*self.r
  print("Area is: ",a)

c=Circle()
c.displayData()
c.area()