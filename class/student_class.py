class Student:
 college="MIT" #class variable
 def __init__(self,rollno,name,branch):
  self.rollno=rollno #instance variable
  self.name=name
  self.branch=branch
  

 def displayData(self):
    print("Student Roll Number: ",self.rollno);
    print("Student Name: ",self.name);
    print("Student Branch: ",self.branch);
    print("Student College Name: ",Student.college)

    print("--------------------------------------------------")
#object of student class

a=Student(101,"PRITI","IT")
p=Student(102,"PRIYANKA","COMPUTER")

a.displayData();
p.displayData();

Student.college='Zeal College'

x=Student(103,"RAM","IT")
y=Student(104,"ALLEN","COMPUTER")

x.displayData();
y.displayData();
