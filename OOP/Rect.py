class Rect:

 def setData(self,l,b):
  self.length=l
  self.bridth=b

 def showData(self):
  print("Length is: ",self.length)
  print("Bridth is: ",self.bridth)

 def area(self):
  a=self.length * self.bridth
  print("Area is: ",a)

 def perimeter(self):
  p=2*(self.length + self.bridth)
  print("Perimeter is: ",p)

r=Rect()
r.setData(5,2)
r.showData()

r.area()
r.perimeter()


