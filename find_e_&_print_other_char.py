str="Welcome"
print("The string is: ",str)

i=0
c=0
x=0

while(str[i:]):
 if(str[i]=='E' or str[i]=='e'):
  c=c+1
 else:
  x=x+1
  print(str[i],end=" ")
 i=i+1



print("\nNumber of e: ",c)
print("Other Character is: ",x)
