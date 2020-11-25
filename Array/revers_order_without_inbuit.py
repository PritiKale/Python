import array as arr
x=arr.array('i',[10,20,30,40,50])

i=0
c=0
while(x[i:]):
 c=c+1
 i=i+1

print("Total elements are: ",c)
print("Array element is reverse order ")

z=c-1
while(x[z:]):
  print(x[z],end=" ")
  z=z-1
  if(z==-1):
   break;   

	