class Box:

 def setData(self,l,b,h):
  self.length=l
  self.bridth=b
  self.heigth=h

 def showData(self):
  print("length is: ",self.length)
  print(" bridth is: ",self.bridth)
  print("heigth is: ",self.heigth)

 def volume(self):
  volume=self.length *  self.bridth * self.heigth
  print("volume is: ",volume)

b=Box()
b.setData(2,3,4)
b.showData()
print("-----------------")
b.volume()

