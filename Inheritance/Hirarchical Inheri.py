class RBI_Bank:
  def getdata(self):
    self.bankname=input("Enter the Bank name :")
    self.location=input("Enter the location :")
    
  def show(self):
    print("Bank name is: ",self.bankname)
    print("Location is: ",self.location)
    

class Saving_Account(RBI_Bank):
  def getdata(self):
    super().getdata()
    self.accno=int(input("Enter the Account no: "))
    self.name=input("Enter the name: ")
    self.bal=int(input("Enter the balance: "))
    
  def show(self):
    super().show()
    print("Account number is: ",self.accno)
    print("Bank name is: ",self.name)
    print("Balance is: ",self.bal)
       
  def deposit(self):
    damt=int(input("Enter the deposit amount: "))
    self.bal=self.bal+damt

  def withdraw(self):
    wamt=int(input("Enter the withdraw amount: "))
    self.bal=self.bal-wamt

  def showbal(self):
    print("Balance after transaction is: ",self.bal)

class Mutual_fund(RBI_Bank):
  def getdata(self):
    self.lumsum_amt=int(input("Enter the lumsum_amt: "))
    self.no_of_year=int(input("Enter the no_of_year: "))

  def show(self):
    print("lumsum_amt is : ",self.lumsum_amt)
    print("no_of_year is : ",self.no_of_year)

  def maturity(self):
   if(self.no_of_year>=10):
    i_amt=(self.lumsum_amt*0.5)*self.no_of_year
    tot_amt=self.lumsum_amt+i_amt
    print("intrest amt is : ",i_amt)
    print("total amt is : ",tot_amt)


   elif(self.no_of_year>=5):
    i_amt=(self.lumsum_amt*0.10)*self.no_of_year
    tot_amt=self.lumsum_amt+i_amt
    print("intrest amt is : ",i_amt)
    print("total amt is : ",tot_amt)



   elif(self.no_of_year>=3):
    i_amt=(self.lumsum_amt*0.20)*self.no_of_year
    tot_amt=self.lumsum_amt+i_amt
    print("intrest amt is : ",i_amt)
    print("total amt is : ",tot_amt)



   elif(self.no_of_year>=1):
    i_amt=(self.lumsum_amt*0.30)*self.no_of_year 
    tot_amt=self.lumsum_amt+i_amt
    print("intrest amt is : ",i_amt)
    print("total amt is : ",tot_amt)



   else:
    print("invalid year....")

choice=int(input("Press 1 for Saving_Account & press 2 for Mutual_fund"))
if(choice==1):
 s=Saving_Account()
 s.getdata()
 s.show()
 print("---------------------------------")

 s.deposit()
 s.show()
 print("---------------------------------")

 s.withdraw()
 s.show()
 print("---------------------------------")

elif(choice==2):
 m=Mutual_fund()
 m.getdata()
 print("---------------------------------")
 
 m.show()

 m.maturity()
 print("---------------------------------")
    
else:
 print("Invalid year")    

       


  

