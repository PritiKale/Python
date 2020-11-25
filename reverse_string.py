str=input("Enter the string: ")

i=0
c=0

while(str[i:]):
 c=c+1
 i=i+1

#print("Length is: ",c)

x=c-1
while(str[x:]):
 print(str[x],end=" ")
 x=x-1
 if(x==-1):
  break

