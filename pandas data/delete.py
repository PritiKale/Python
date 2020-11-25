import pandas as pd
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
 'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
 'three' : pd.Series([10,20,30], index=['a','b','c'])}
df = pd.DataFrame(d)
print ("Our dataframe is:")
print (df)

print("----------------------------------------")

print ("Deleting the first column using DEL function:")
del df['one']
print (df)

print("----------------------------------------------")

print ("Deleting another column using POP function:")
df.pop('two')
print (df)