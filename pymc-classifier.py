# >>TITLE - Python Machine Learning Classifier Introduction

# >>BREADCRUMB - HOME,http://www.tinitiate.com, scripting Languages,/scripting-languages/, PYTHON,/tutorials/python, MACHINE-LEARNING-CLASSIFIER-INTRO,*


# >>HEADLINE - Python Machine Learning Classifier Introduction
# >>AUTHOR - Venkata Bhattaram / TINITIATE.COM
# >>DATEPUBLISHED - 2016-07-11


# >>DESC<<
# Python Machine Learning Supervised learning Classifier Introduction
# >><<


# >>KEYWORDS<<
# Python Machine Learning Supervised learning Classifier Introduction
# >><<


# >>POINTS -
# + Supervised machine learning is the process of correctly determining the 
#   classification of a given dataset.
# + This requires a example training dataset pair,
#   Each example is a pair consisting of an input object (typically a vector) 
#   and a desired output value (also called the supervisory signal). 
# + The data set comprises of Features and Labels
# + Classification: Identifying to which category or classification a test data set 
#   belongs to.
# + Features:
#   Feature is an individual measurable properties about a test "subject" 
#   that are passed to the machine learning alogrithm.
#   Getting the properties for features right is very crucial, for effective 
#   algorithms in machine learning.
# + Labels:
#   Labels are the targets the features represent.
#   
# >><<


# >>FILE-NAME - pymc1-classifier.py
# >>DEPENDANT-FILES - N/A
from sklearn import tree




# >>CODE-TITLE - Python Machine Learning Regression Introduction
# >>CODE-NOTES<<
# Python Machine Learning Regression Introduction
# >><<
# >>CODE-PYTHON-ALL<<


# Classifier
# This is a box of rules
# Features About the Label, There can be multiple features for a Label
# Label is the entity which needs to be classified to. 

# Smart Phone OS Prediction
# Android or Windows
# Features
# 1XXXX = iPhone
# 2XXXX = Android
# 1     = Single Side Charger
# 2     = Two Side Charger

# labels 
# 1 = iPhone
# 2 = Android

# Training
features = [[1223,1],[1556,2],[1234,2],[2222,1],[2456,1]]
labels   = [1,1,1,2,2]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# Feeding Data by KNN [Known Nearest Neighbours] Method

# Testing
print(clf.predict([[2345,2]]))
print(clf.predict([[1445,2]]))
# >><<
# >>OUTPUT<<
# [2]
# [1]
# >><<



# >>CODE-TITLE - Python Machine Learning Regression Introduction
# >>CODE-NOTES<<
# Python Machine Learning Regression Introduction
# >><<
# >>CODE-PYTHON-ALL<<
from sklearn import ensemble

# Classifier
# This is a box of rules
# Features About the Label, There can be multiple features for a Label
# Label is the entity which needs to be classified to. 

# Smart Phone OS Prediction
# Android or Windows
# Features
# 1XXXX = iPhone
# 2XXXX = Android
# 1     = Single Side Charger
# 2     = Two Side Charger

# labels 
# 1 = iPhone
# 2 = Android

# Training
features = [[1223,1],[1556,2],[1234,2],[2222,1],[2456,1]]
labels   = [1,1,1,2,2]

rf  = ensemble.RandomForestRegressor()
rf.fit(features, labels)

# Feeding Data by KNN [Known Nearest Neighbours] Method

# Testing
print(rf.predict([[2345,2]]))
print(rf.predict([[1445,2]]))

for depth in range(1,10):

    tree_classifier = tree.DecisionTreeClassifier(
    max_depth=depth, random_state=0)

    if tree_classifier.fit(features, labels).tree_.max_depth < depth:
        break
        score = np.mean(cross_val_score(tree_classifier, features, labels, scoring=‘accuracy’, cv=crossvalidation, n_jobs=1))
        print ‘Depth: %i Accuracy: %.3f’ % (depth,score)

# >><<
# >>OUTPUT<<
# [2]
# [1]
# >><<

