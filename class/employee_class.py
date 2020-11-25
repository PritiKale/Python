class Employee:
 city="PUNE" #class variable
 def __init__(self,empid,ename,job,sal):
  self.empid=empid #instance variable
  self.ename=ename
  self.job=job
  self.sal=sal

 def showData(self):
    print("Employee Id: ",self.empid);
    print("Employee Name: ",self.ename);
    print("Employee Job: ",self.job);
    print("Employee Salary: ",self.sal);
    print("Employee City: ",Employee.city)

    print("--------------------------------------------------")
#object of student class

a=Employee(1001,"Priti","Clerk",30000)
p=Employee(1002,"Priyanka","Developer",40000)
k=Employee(1001,"Ratan","Analyst",35000)

a.showData();
p.showData();
k.showData();






