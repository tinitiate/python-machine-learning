import matplotlib.pyplot as plt
import numpy as np
import scipy, pylab


"""
# Creating a Scatter Plot
# -----------------------

marker=['O','X','^']
plt.scatter( [1,2,3]
            ,[4,5,6]
            ,500
            ,color=['red','green','blue']
            ,marker)




plt.scatter( [1,2,3,4,5,6,7,8,1,2,2,3]
            ,[4,5,6,3,4,5,6,7,8,6,8,9]
            ,20
            ,cmap=plt.cm.Paired)


plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.show()



num_of_lines = 3

x = np.arange(10)
y = []

# For each line
for i in range(num_of_lines):
    # Adds to y according to y=ix+1 function
    y.append(x*i+1)

print(x)
print(y)
"""


# Adding Multiple Sets to a Scatter Plot
# --------------------------------------
plt.scatter( [1,2,3,4,5,6,7,8,1,2,2,3]
            ,[4,5,6,3,4,5,6,7,8,6,8,9]
            ,150
            ,marker="^"
            ,color="lightblue")

plt.scatter( [1,2,3,4,5,6,7,8,1,2]
            ,[11,12,11,14,14,13,15,15,16,16]
            ,75
            ,marker="^"
            ,color="violet")

plt.scatter( [1,2,3,4,5,6,7,8,1,2]
            ,[21,22,21,24,24,23,25,25,26,26]
            ,200
            ,marker="^"
            ,color="pink")

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')           
            
plt.show()
