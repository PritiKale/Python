str=input("Enter the Name in lowercase: ")
print("The string is: ",str)

i=0

while(str[i:]):
 print(chr(ord(str[i])-32),end=" ")
 i=i+1