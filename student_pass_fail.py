name=input("Enter the name: ")
chem=int(input("Enter the chem marks: "))
math=int(input("Enter the math's marks: "))
phy=int(input("Enter the phy marks : "))
php=int(input("Enter the php marks: "))
java=int(input("Enter the java marks: "))

print(" ")

print("name is: ",name)
print("chem marks is: ",chem)
print("math is: ",math)
print("phy  marks is: ",phy)
print("php marks is: ",php)
print("java marks is: ",java)

print(" ")

marks=chem+math+phy+php+java
print("total marks is: ",marks)

print(" ")

per=marks/5
print("percentage is: ",per)

print(" ")


if(chem>=40 and math>=40 and phy>=40 and php>=40 and java>=40):
	print("candidate is pass")
else:
	print("candidate is fail")