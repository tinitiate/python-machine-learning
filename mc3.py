from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
import numpy as np

data = load_boston()
print(data.keys())

print(data.data.shape)
print(data.target.shape)

# print(data.DESCR)

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

print(X_train)
print(y_train)

print(X_test)
print(y_test)

"""
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

clf = LinearRegression()
clf.fit(X_train, y_train)

# predicted = clf.predict(X_test)
# expected  = y_test

# print(predicted)
# print(expected)


plt.scatter(expected, predicted)
plt.plot([0, 50], [0, 50], '--k')
plt.axis('tight')
plt.xlabel('True price ($1000s)')
plt.ylabel('Predicted price ($1000s)')

plt.show()

print("RMS:", np.sqrt(np.mean((predicted - expected) ** 2)))
"""