class Student:

  def getData(self):
   self.rollno=input("Enter the rollno: ")
   self.name=input("Enter the name: ")
   self.branch=input("Enter the branch: ")
   self.phy=int(input("Enter the physics: "))
   self.che=int(input("Enter the chemistry: "))
   self.math=int(input("Enter the maths: "))

  def showData(self):
   print("Roll Number is: ",self.rollno)
   print("Student Name is: ",self.name)
   print("Branch is: ",self.branch)
   print("Physics marks is: ",self.phy)
   print("Chemistry marks is: ",self.che)
   print("Maths marks is: ",self.math)


  def totalmarks(self):
   total=self.phy + self.che + self.math
   print("Total marks: ",total)

  def percentage(self):
   per=(self.phy + self.che + self.math)/3
   print("percentage: ",per)


s=Student()
s.getData()
print("---------------------Student Information-------------------")
s.showData()
print("------------------------------------------")
s.totalmarks()
s.percentage()
