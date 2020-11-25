import pandas as pd
s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.swapcase())

print("-----------------------------------------")

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.islower())

print("-----------------------------------------")

s = pd.Series(['tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.islower())

print("-----------------------------------------")

s = pd.Series(['TOM', 'William Rick', 'John', 'Alber@t'])
print (s.str.isupper())

print("-----------------------------------------")

s = pd.Series(['12345', 'William Rick', 'John', 'Alber@t'])
print (s.str.isnumeric())
