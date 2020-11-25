import array as arr
a=arr.array('i',[10,20,30,40,50,60,70,80])
print(a)
a[0]=100
print(a)
a[2:5]=arr.array('i',[500,600,700])	#change 3rd to 5th element
print(a)