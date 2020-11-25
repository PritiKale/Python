import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print ("The number of 'm's in each string:")
print (s.str.count('m'))