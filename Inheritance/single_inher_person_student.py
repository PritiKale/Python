class Person:
 def getData(self):
  self.name=input("Enter the name:")
  self.city=input("Enter the city:")
  self.age=int(input("Enter the age:"))

 def showData(self):
  print("Name: ",self.name)
  print("City: ",self.city)
  print("Age: ",self.age)




class Student(Person):
 def readData(self):
  super().getData()
  self.rollno=int(input("Enter the Rollno:"))
  self.mark=int(input("Enter the Marks:"))
  self.branch=input("Enter the Branch:")


 def display(self):
  super().showData()
  print("Rollno: ",self.rollno)
  print("Marks: ",self.mark)
  print("Branch: ",self.branch)





s=Student()
s.readData()
s.display()