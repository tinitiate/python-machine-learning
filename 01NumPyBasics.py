import numpy as np

#  Create a Random 3X5 Matrix
X=np.random.random((3,5))

print(X)


# Accessing elements

# get a single element
print(X[0, 0])

# get a row
print(X[1])

# get a column
print(X[:, 1])

# Transposing an array
print(X.T)

# LinSpace Divide Start and End in equal parts, 
# with the last parameter number if intervals
y = np.linspace(0, 50, 5)
print(y)

y = np.linspace(0, 40, 5)
print(y)

y = np.linspace(0, 60, 5)
print(y)


# make into a column vector
print(y[:, np.newaxis])

# getting the shape or reshaping an array
print(X.shape)
print(X.reshape(5, 3))
