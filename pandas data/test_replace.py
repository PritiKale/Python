import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s)
print ("After replacing @ with $:")
print (s.str.replace('@','$'))