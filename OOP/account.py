class Account:

 def getData(self):
  self.accno=input("Enter Account number: ")
  self.name=input("Enter name: ")
  self.bal=int(input("Enter balance: "))
  self.city=input("Enter city: ")

 def showData(self):
  print("Account number : ",self.accno)
  print("Name : ",self.name)
  print("Balance: ",self.bal)
  print("City: ",self.city)

 def deposite(self):
  damt=int(input("Enter the amount for deposite: "))
  self.bal=self.bal+damt;

 def withdrow(self):
  wamt=int(input("Enter the withdrow amount: "))
  if wamt>self.bal:
  	print("you have insufficient balance")
  else:
  	self.bal=self.bal-wamt

 def showbal(self):
  print("Balance after transaction: ",self.bal)


a=Account()

a.getData()
a.showData()

print("-------------------------------------")

a.deposite()
a.showbal()

print("--------------------------------------")

a.withdrow()
a.showbal()