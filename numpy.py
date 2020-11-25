import numpy as np

a=np.array([[1,2,3,4],[9,0,2,3],[1,2,3,19]])

print("The Original Array:\n")
print(a)


b=a.copy()

print("\n Printing the deep copy b")
print(b)

b.shape=4,3;

print("\n Change made to the copy b do not reflect a")
print("\n Original  array\n",a)
print("\n copy \n ",b)

