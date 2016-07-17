# Support Vector machine
# Inputs a 2d Array and 1D array as Inputs
# Vectorization or Feature Extraction, COnvert Text and Image data into
# Array data for machie learning
# samples 1D
# Features 2D


from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.datasets import get_data_home
import matplotlib.pyplot as plt

iris = load_iris()
iris.keys()

n_samples, n_features = iris.data.shape

print(n_samples)
print(n_features)
print(iris.data[0])

print(iris.data.shape)
print(iris.target.shape)

print(iris.target)
print(iris.target_names)

# These are the Feature Columns that will be used to plot the graph
# Change between 0-3
x_index = 2
y_index = 3

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(iris.data[:, x_index], iris.data[:, y_index],250, c=iris.target)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])
plt.show()
