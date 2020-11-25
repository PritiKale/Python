class Emp_Payment:
 def getData(self):
  self.empid=input("Enter employee id: ")
  self.name=input("Enter name: ")
  self.job=input("Enter job: ")
  self.basic_sal=int(input("Enter basic salary: "))

 def showData(self):
  print("Emp id : ",self.empid)
  print("Employee name : ",self.name)
  print("Employee job : ",self.job)
  print("Employee basic salary : ",self.basic_sal)

 def hra_fun(self):
  hra_amt=self.basic_sal * 0.30
  return hra_amt

 def ta_fun(self):
  ta_amt=self.basic_sal * 0.20
  return ta_amt

 def pf_fun(self):
  pf_amt=self.basic_sal * 0.10
  return pf_amt

 def payment(self,hamt,tamt,pamt):
  tpay=self.basic_sal+hamt+tamt+pamt
  print("Total Payment: ",tpay)


ep=Emp_Payment()
ep.getData()
ep.showData()

hamt=ep.hra_fun()
tamt=ep.ta_fun()
pamt=ep.pf_fun()

print("Hra amount is : ",hamt)
print("Ta amount is : ",tamt)
print("Pf amount is : ",pamt)

ep.payment(hamt,tamt,pamt)

