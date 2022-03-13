print("Name: Sumit Singh\nRollNo:4354\n")
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('pokemon.csv')
df
kmeans_model = KMeans(n_clusters=6,max_iter=1000)
kmeans_model.fit(df[['HP','Attack']])
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=1000,
       n_clusters=6,	n_init=10,random_state=None, tol=0.0001, verbose=0)
color_dictionary = {0: 'red', 1: 'blue', 2: 'green' , 3: 'yellow',4: 'pink', 5: 'black'}
label_list = kmeans_model.labels_.tolist()
df['color'] = label_list

for i in color_dictionary:
    df['color'] = df['color'].replace(i,color_dictionary[i])

y = df['HP']
x = df ['Attack']

fig, ax = plt.subplots()
ax.scatter(x, y,c = df['color'], s = 100)
ax.legend()
plt.show()
