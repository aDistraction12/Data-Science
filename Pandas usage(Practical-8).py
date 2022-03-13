print("Name: Sumit Singh\nRollNo:4354\n")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('pokemon.csv') #usage of pandas df.head()
df.drop('#', inplace=True, axis=1)
df.head()
df.shape #usage of numpy

df.info()

newdf = pd.DataFrame(df, columns=['Name','HP'])
newdf.head()
newdf.shape
plt.rcParams["figure.figsize"] = (20, 9)
plt.scatter(newdf['Name'].head(), newdf['HP'].head())
plt.show()
