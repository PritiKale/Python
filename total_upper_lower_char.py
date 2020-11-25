str="Welcome To Pune"
print("The string is: ",str)

i=0
u=0
l=0

while(str[i:]):
 if(ord(str[i])>=65  and ord(str[i])<=90 ):
  u=u+1
 if(ord(str[i])>=97  and ord(str[i])<=122 ):
  l=l+1

 i=i+1

print("Total uppercase: ",u)
print("Total lowercase: ",l)
