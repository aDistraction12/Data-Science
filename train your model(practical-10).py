print("Name: Sumit Singh\nRollNo:4354\n")
import pandas as pd
from sklearn.datasets import load_iris
iris_data = load_iris()
df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
print(df)
from sklearn.model_selection import train_test_split
training_data, testing_data = train_test_split(df, test_size=0.2, random_state=25)
#random state is used to keep the data constant if it is 0 then everytime u run
#the program the value of data changes.
print(f"No. of training examples: {training_data.shape[0]}")
print(f"No. of testing examples: {testing_data.shape[0]}")
training_data.head()
