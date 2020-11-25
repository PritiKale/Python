import array as arr
x=arr.array('d',[1.5,2.5,3.5,4.5,5.5])

i=0
c=0
print("Elements are: ")

while(x[i:]):
 print(x[i],end=" ")	
 c=c+1
 i=i+1
#print("\ncount is: ",c)

print("\n Elements in Reverse order ")


z=c-1
while(x[z:]):
 print(x[z],end=" ")
 z=z-1
 if(z==-1):
  break;