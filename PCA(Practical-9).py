print("Name: Sumit Singh\nRollNo:4354\n")
import pandas as pd
import matplotlib.pyplot as plt
#Standarized the dataset features
from sklearn.preprocessing import StandardScaler
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# load dataset into Pandas DataFrame
df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])
df.head()
mean_sepal_length = df['sepal length'].mean()
mean_sepal_length
std_dev_sepal_length = df['sepal length'].std()
std_dev_sepal_length
(5.1-mean_sepal_length)/std_dev_sepal_length
feature = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:,feature]
y = df.loc[:,'target']
x = StandardScaler().fit_transform(x)
standardised_values = pd.DataFrame(x,columns=feature)
standardised_values
#PCA PROJECTION OF 2D
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pct = pca.fit_transform(x)
principal_df = pd.DataFrame(pct,columns=['pc1','pc2'])
#CONCATINATING TARGET
finaldf= pd.concat([principal_df,df[['target']]],axis=1)
finaldf.head()
#PLOTTING 2 DIEMENTIONAL DATA
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finaldf['target'] == target
    ax.scatter(finaldf.loc[indicesToKeep, 'pc1']
        , finaldf.loc[indicesToKeep, 'pc2']
        , c = color
        , s = 50)
ax.legend(targets)
ax.grid()
#SHOWS TWO SEPARATE VARIENCE PERCENT
pca.explained_variance_ratio_
