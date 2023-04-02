'''
estmate.py
    This script estimates the number of tigers in the census data
Usage:
    python estimate.py'''


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the train dataset
df = pd.read_csv('Train.csv')
df = df.drop(['Trail','Soil','Left'], axis = 1) 

# Split the data into training and testing sets
X = df.drop('Distinct', axis = 1)
y = df['Distinct']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

# Train the K-Nearest Neighbor model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Test the model on the test data
y_pred = knn.predict(X_test)
print("Accuracy of KNN on test data: ", accuracy_score(y_test, y_pred))


# Load test data
new_data = pd.read_csv('Census.csv')

# Predict the values using the trained KNN model
new_data['Distinct'] = knn.predict(new_data)

# Print the sum of the values in the predicted column -> Total number of tigers
print("Total predicted number of Tigers is: ", new_data['Distinct'].sum())
