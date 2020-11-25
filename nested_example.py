name=input("Enter the name: ")
phy=int(input("Enter the phy marks: "))
chem=int(input("Enter the chem marks : "))
math=int(input("Enter the math's marks: "))
c=0

print(" ")

print("name is: ",name)
print("phy marks is: ",phy)
print("chem is: ",chem)
print("math  marks is: ",math)

print(" ")

marks=phy+chem+math
print("total marks is: ",marks)

print(" ")

per=marks/3
print("percentage is: ",per)

print(" ")


if(phy>=40 and chem>=40 and math>=40):
	print("student is pass")
	if(per>=60):
	 print("student get 1st class")	

else:
	print("candidate is fail")
if(phy<40):
     print("student is fail in phy")
     c=c+1
if(chem<40):
     print("student is fail in chem")
     c=c+1
if(math<40):
     print("student is fail in math's")
     c=c+1

print(" Fail in total no of sub ",c)  


