print("Name: Sumit Singh\nRollNo:4354\n")
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
apples_oranges = pd.read_csv("apples_and_oranges.csv")
apples_oranges.head()
# create a dictionary to colour classes
color_dict = dict({'orange':'orange','apple':'green'})
# scatterplot
plt.xlabel('Weight')
plt.ylabel('Size')
plt.title('Sizes and Weights of apples and oranges')
sns.scatterplot(data=apples_oranges, x="Weight", y="Size", hue="Class", palette = color_dict)
plt.show()
# define input data

X = apples_oranges[["Weight", "Size"]] # define target
y = apples_oranges.Class

# fitting the support vector machine using a linear kernel
from sklearn import svm
clf = svm.SVC(kernel = 'linear', C=10)
clf.fit(X, y)
b = clf.intercept_
w_1 = clf.coef_[0][0]
w_2 = clf.coef_[0][1]
b, w_1, w_2
# plotting the hyperplane and support vector lines
ax = plt.gca()
sns.scatterplot(data=apples_oranges, x="Weight", y="Size", hue="Class", palette = color_dict)
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY,XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T

Z = clf.decision_function(xy).reshape(XX.shape)
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
linestyles=['--', '-', '--'])

ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k')
 
plt.show()

# obtain support vectors
clf.support_vectors_
clf.predict([[70, 4.6]])
