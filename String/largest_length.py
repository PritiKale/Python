str1=input("Enter the first name: ")
str2=input("Enter the second name: ")

print(str1)
x=0

print(str2)
y=0

#for loop for 1st string
for i in str1:
	x=x+1;
print("length of 1st no is : ",x)

#for loop for 2nd string
for i in str2:
	y=y+1;
print("length of 2nd no is : ",y)

if(x>y):
 print("Largest length is: ",x)

elif(x<y):
 print("Largest length is: ",y)

else:
 print("Both are same")

