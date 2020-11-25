class Abc:
 def __init__(self):
  self.a=int(input("Enter the number:"))

class Xyz(Abc):
 def getData(self):
  self.b=int(input("Enter the number:"))

 def sum(self):
  s=self.a + self.b
  print("Sum is: ",s)





x=Xyz()
x.getData()
x.sum()