import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print (s.str.findall('e'))