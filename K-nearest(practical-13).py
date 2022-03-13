# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')

#X contains the attributes.
#Because we don’t want to take in consideration the first two columns, we will copy only column 2 and 3
X = dataset.iloc[:, [2, 3]].values

#The labels are in the 4th column, so we will copy this column in variable y
y = dataset.iloc[:, 4].values

#sklearn has the method called train_test_split, which will split our data set returning 4 values
from sklearn.model_selection import train_test_split

#25% of the data set for test and 75% for train. 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#Distance is much heigher between salary and age column to resolve this issue we used standardscaler.
from sklearn.preprocessing import StandardScaler
print("Name: Sumit Singh\nRollNo:4354\n")
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#importing the KNeighborsClassifier from sklearn. This takes multiple parameters.
#n_neighbors,algoritm(for design structure),matric (for distance by default euclidean, Manhattan)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 2)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix to check the accuracy
#TP+TN/TP+FN+FP+TN (formula TP=true positive,
#FN=false negative,[Observation is positive, but is predicted negative]
#TN=true negative, [ Observation is negative, and is predicted to be negative]
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Visualising the Training set results
#meshgrid() creates a rectangular grid out of an array of x values and an array of y values here x = X1 and y = X2
#contourf method use to fill the background with the color of the class
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Classifier (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend() #use  to Place a legend on the axes.
plt.show()
