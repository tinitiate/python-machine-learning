# >>TITLE - Python Machine Learning Regression Introduction

# >>BREADCRUMB - HOME,http://www.tinitiate.com, scripting Languages,/scripting-languages/, PYTHON,/tutorials/python, MACHINE-LEARNING-REGRESSION-INTRO,*


# >>HEADLINE - Python Machine Learning Regression Introduction
# >>AUTHOR - Venkata Bhattaram / TINITIATE.COM
# >>DATEPUBLISHED - 2016-07-11


# >>DESC<<
# Python Machine Learning Supervised learning Regression Introduction
# >><<


# >>KEYWORDS<<
# Python Machine Learning Supervised learning Regression Introduction
# >><<


# >>POINTS -
# + Supervised machine learning is the process of correctly determining the 
#   classification of a given dataset.
# + This requires a example training dataset pair,
#   Each example is a pair consisting of an input object (typically a vector) 
#   and a desired output value (also called the supervisory signal). 
# + Regression: Predicting a continuous-valued attribute associated with an object.
# >><<


# >>FILE-NAME - pymc2-regression.py
# >>DEPENDANT-FILES - N/A



# >>CODE-TITLE - Python Machine Learning Regression Introduction
# >>CODE-NOTES<<
# Demonstration Python Machine Learning Regression Introduction
# >><<
# >>CODE-PYTHON-ALL<<
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

# >><<

# >>TAGS -  Python machine learning SCIKIT Regression
