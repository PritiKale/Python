str="India"
print("The string is: ",str)

i=0
c=0
x=0

while(str[i:]):
 if(str[i]=='i' or str[i]=='I'):
  c=c+1
 else:
  x=x+1
 i=i+1



print("Number of I: ",c)
print("Other Character is: ",x)
