name=input("Enter the name: ")
chem=int(input("Enter the chem marks: "))
math=int(input("Enter the math's marks: "))
phy=int(input("Enter the phy marks: "))
java=int(input("Enter the java marks: "))
css=int(input("Enter the css marks: "))
c=0

print("---------------------------------------")

print("name: ",name)
print("chem marks : ",chem)
print("math's marks: ",math)
print("phy marks: ",phy)
print("java marks: ",java)
print("css marks: ",css)

print("---------------------------------------")


total_marks=chem+math+phy+java+css
print("Total marks: ",total_marks)

percentage=total_marks/5
print("percentage: ",percentage)

if(chem>=40 and math>=40 and phy>=40 and java>=40 and css>=40):
 print("student is pass")
 
else:
 print("Candidate is fail")
 if(chem<40):
  print("student fail in chemistry") 
  c=c+1
 if(math<40):
  print("student fail in math") 
  c=c+1
 if(phy<40):
  print("student fail in phy") 
  c=c+1
 if(java<40):
  print("student fail in java") 
  c=c+1
 if(css<40):
  print("student fail in css") 
  c=c+1

 print("fail in total sub: ",c)

