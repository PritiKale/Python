import pandas as pd
s = pd.Series(['Martin', 'Turner', 'John', 'Alber@t','Smith'])
print (s)

print("----------------------------------")

s = pd.Series(['Tom', 'Rick', 'John','Smith'])
print (s.str.lower())

print("----------------------------------")

s = pd.Series(['Tom', ' Rick', 'John', ])
print (s.str.upper())

print("----------------------------------")


s = pd.Series(['Akshay', 'Ram','Rahul'])
print (s.str.len())

print("----------------------------------")


s = pd.Series(['Tom ', 'Rick', 'John', 'Alber@t'])
print (s)
print ("After Stripping:")
print (s.str.strip())

print("----------------------------------")


s = pd.Series(['Toml', 'Rick', 'Johnl', 'Alber@t'])
print (s)
print ("Split Pattern:")
print (s.str.split('l'))

print("----------------------------------")

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.cat(sep='_'))

print("----------------------------------")

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.contains(' '))

print("----------------------------------")



