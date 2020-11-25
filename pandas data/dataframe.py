import pandas as pd
data = [['Alex',10,'mumbai'],
 ['Bob',12,'pune'],
 ['Clarke',13,'Nashik']]
df = pd.DataFrame(data,columns=['Name','Age','city'])
print (df)