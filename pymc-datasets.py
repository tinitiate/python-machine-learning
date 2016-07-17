# >>TITLE - Python Machine Learning DataSets

# >>BREADCRUMB - HOME,http://www.tinitiate.com, scripting Languages,/scripting-languages/, PYTHON,/tutorials/python-machine-learning, DATASETS,*


# >>HEADLINE - Python Machine Learning DataSets
# >>AUTHOR - Venkata Bhattaram / TINITIATE.COM
# >>DATEPUBLISHED - 2016-07-12


# >>DESC<<
# Python Machine Learning DataSets
# >><<


# >>KEYWORDS<<
# Python, Machine Learning, DataSets
# >><<


# >>POINTS<<
# + Python Machine Learning DataSets
# >><<


# >>FILE-NAME - pymc-datasets.py
# >>DEPENDANT-FILES - N/A



# >>CODE-TITLE - Python Machine Learning DataSets
# >>CODE-NOTES<<
# Demonstration of Python Machine Learning DataSets
# >><<
# >>CODE-PYTHON-ALL<<
# Calculates the linear regression model and plots the data
# Limitations: only returns the most basic regression outputs

from sklearn.datasets import load_iris
iris = load_iris()
n_samples, n_features = iris.data.shape


# Samples Rows
print(n_samples)

# Features Columns
print(n_features)


# Columns X Features
print(iris.data)
print(len(iris.data))


# Columns X Features
print(iris.target_names)

# Columns X Features
print(iris.target)
print(len(iris.target))
# >><<
# >>OUTPUT<<
# 
# >><<
