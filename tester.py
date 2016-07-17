from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


xTrain = [[2,4,6],[3,6,9],[4,8,12],[5,10,15]]
yTrain = [2,3,4,5]

xTest  = [[6,12,18],[7,14,21]]
yTest  = [6,7]


clf = LinearRegression()
clf.fit(xTrain, yTrain)

predicted = clf.predict(xTest)
expected  = yTest

print(predicted)
print(expected)

# plt.scatter(expected, predicted)
# plt.plot([0, 20], [0, 20], '--k')

plt.scatter(expected, predicted, marker="^",color="red")
# plt.scatter(yTrain, yTest, marker="X",color="green")

plt.plot([0, 20], [0, 20], '--k')

plt.axis('tight')

plt.xlabel('True price ($1000s)')
plt.ylabel('Predicted price ($1000s)')

plt.show()
