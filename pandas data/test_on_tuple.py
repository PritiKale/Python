num=(10,20,30,40,50)

print(num)

# num[0]=5000
# print(num)

xyz=list(num)
print(xyz)

xyz[0]=5000
num=tuple(xyz)
print(num)

#how to remove the element
mylist=list(num)

mylist.remove(30)

num=tuple(mylist)
print(num)