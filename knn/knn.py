import numpy as np
from collections import Counter
def euclideands(self,x1,x2):
    return np.sqrt(sum((x1-x2)**2))


class KNN:
    def __init__(self,k=3):
        self.k = k


    def fit(self,X,y):

        self.xtrain = X
        self.ytrain = y
    


    def predct(self,X):
        predcts=[self._predct(x) for x in X]
        return predcts


    def _predct(self,x):
        dest = [self.euclideands(x,xtrain) for xtrain in self.xtrain]
        kees=np.argsort(dest)[:self.k]
        klabel= [self.ytrain[i] for i in kees]
        mostco = Counter(klabel).most_common(1)
        return mostco[0][0]
    


    def euclideands(self,x1,x2):             
        return np.sqrt(sum((x1-x2)**2))




# Simple 2D data test case
X_train = np.array([[1, 2], [2, 3], [3, 4], [6, 8], [7, 9], [8, 8]])
y_train = np.array([0, 0, 0, 1, 1, 1])

knn = KNN(k=3)
knn.fit(X_train, y_train)

# Test cases: single points and multiple points
X_test = np.array([[4, 4], [5, 5], [0, 0]])

# Expected result: [0, 1, 0] (0 for [4, 4] as it's closer to class 0 points)
predictions = knn.predct(X_test)
print(f"Predictions for X_test [[4, 4], [5, 5], [0, 0]]: {predictions}")
# All training data belongs to the same class
X_train = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
y_train = np.array([1, 1, 1, 1])

knn = KNN(k=2)
knn.fit(X_train, y_train)

# Since all points are class 1, every prediction should also be class 1
X_test = np.array([[1, 2], [3, 4]])
predictions = knn.predct(X_test)
print(f"Predictions for X_test [[1, 2], [3, 4]] (all same class): {predictions}")
# Edge case where k is larger than the number of training points
X_train = np.array([[1, 2], [3, 4], [5, 6]])
y_train = np.array([0, 1, 0])

knn = KNN(k=5)  # k is larger than the number of points (3)
knn.fit(X_train, y_train)

# Test a point close to [3, 4]
X_test = np.array([[4, 5]])
predictions = knn.predct(X_test)
print(f"Predictions for X_test [[4, 5]] (k > n): {predictions}")
# Test with higher-dimensional data (e.g., 5D)
X_train = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [5, 6, 7, 8, 9]])
y_train = np.array([0, 0, 1])

knn = KNN(k=2)
knn.fit(X_train, y_train)

# Test data in 5D space
X_test = np.array([[3, 4, 5, 6, 7], [1, 1, 1, 1, 1]])
predictions = knn.predct(X_test)
print(f"Predictions for 5D X_test [[3, 4, 5, 6, 7], [1, 1, 1, 1, 1]]: {predictions}")

