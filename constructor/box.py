class Box:
 
 def __init__(self,l,b,h):  #construtor with parameter
  self.len=l
  self.bre=b
  self.hei=h

 def volume(self):
  v=self.len * self.bre * self.hei
  print("Volume is: ",v)

b=Box(5,5,5)
b.volume()