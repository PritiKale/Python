class Emp:
 
 def __init__(self,empid,nm,job,sal):
  self.eid=empid
  self.name=nm
  self.job=job
  self.salary=sal

 def showData(self):
  print("Employee empid: ", self.eid)
  print("Employee name: ",self.name)
  print("Employee job: ",self.job)
  print("Employee salary: ",self.salary)

e=Emp(101,'PRITI','DEVELOPER',20000)
e.showData()

print("---------------------------------------")

e1=Emp(102,'ASHOK','DEVELOPER',30000)
e1.showData()

