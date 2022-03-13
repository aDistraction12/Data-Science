print("Name: Sumit Singh\nRoll No:4354")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon.csv') #usage of pandas
df.head()
df.drop('#', inplace=True, axis=1)
df.head()
df.shape #usage of numpy

# frame[‘DataFrame Column’]= frame[‘DataFrame Column’].apply(str)
df['Type 2'] = df['Type 2'].apply(str)

df.info()

newdf = pd.DataFrame(df, columns=['Name','HP'])
newdf.head()
newdf.shape
plt.rcParams["figure.figsize"] = (20, 9)
plt.bar(newdf['Name'].head(), newdf['HP'].head())
plt.show()
