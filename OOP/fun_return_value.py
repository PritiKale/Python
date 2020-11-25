class Testsum:

 def enterData(self):
  self.a=int(input("Enter the 1st value: "))
  self.b=int(input("Enter the 2nd value: "))

 def sum(self):
  z=self.a + self.b
  return z


 def multi(self):
  z=self.a * self.b
  return z

 def div(self):
  z=self.a / self.b
  return z

ts=Testsum()
ts.enterData()

s=ts.sum()
print("sum is: ",s)

m=ts.multi()
print("Multi is: ",m)

d=ts.div()
print("division is: ",d)

