class Emp:
 
 def __init__(self):
  self.empid=input("Enter Employee empid: ")
  self.nm=input("Enter Employee name: ")
  self.job=input("Enter Employee job: ")
  self.sal=int(input("Enter Employee salary: "))

 def showData(self):
  print("Employee empid: ",self.empid)
  print("Employee name: ",self.nm)
  print("Employee job: ",self.job)
  print("Employee salary: ",self.sal)

e=Emp()
e.showData()


