class Person:

 def readData(self):
  self.name=input("Enter the name: ")
  self.city=input("Enter the city: ")
  self.age=input("Enter the age: ")

 def showData(self):
  print("Name is: ",self.name)
  print("City is: ",self.city)
  print("Age is: ",self.age)


p=Person()
print("-----------------------")
p.readData()
p.showData()

print("\n")

p2=Person()
print("-----------------------")
p2.readData()
p2.showData()


p3=Person()
print("-----------------------")
p3.readData()
p3.showData()

