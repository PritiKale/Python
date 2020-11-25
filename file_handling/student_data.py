file=open("student.txt","w")

rollno=int(input("Enter Roll number: "))
name=input(" Student Name is : ")
phy=int(input("Enter phy marks: "))
chem=int(input("Enter chem marks: "))
math=int(input("Enter math's marks: "))

total_marks=phy + chem + math

percentage=total_marks/3

file.write("\n Roll Number: ")
file.write(str(rollno))

file.write("\n Student Name : ")
file.write(name)

file.write("\n Physics Marks : ")
file.write(str(phy))

file.write("\n Chemistry Marks : ")
file.write(str(chem))

file.write("\n Math's Marks : ")
file.write(str(math))

file.write("\n Total Marks: ")
file.write(str(total_marks))

file.write("\n Percentage: ")
file.write(str(percentage))


print("file write sucessfully")
