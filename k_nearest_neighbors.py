"""
file : k_nearest_neighbors.py
author: Petri Lamminho
Simple aapplication witch use K Nearest Neighbors- algorithm
"""
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, neighbors

data_file = "breast-cancer-wisconsin.data"

df = pd.read_csv(data_file) # read data to Pandas-dataframe
df.replace('?', -99999, inplace=True) # replace blank data, "?" to -99999
df.drop(['id'], 1, inplace=True) # drop id column

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])
X_train, X_test,  y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25)

classifier = neighbors.KNeighborsClassifier()
classifier.fit(X_train, y_train)
acc = classifier.score(X_test, y_test)
print(acc)


example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,5,1], [4,2,1,1,1,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures), -1)
prediction = classifier.predict(example_measures)
print(prediction)

