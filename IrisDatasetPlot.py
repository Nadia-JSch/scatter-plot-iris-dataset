# import the iris dataset, matplotlib and numpy
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

# create new figure
fig = plt.figure()

# create 12 subplots with the layout of 4 rows, 3 columns and
# the subplot number passed as arguments
sp1 = plt.subplot(4, 3, 1)
sp2 = plt.subplot(4, 3, 2)
sp3 = plt.subplot(4, 3, 3)
sp4 = plt.subplot(4, 3, 4)
sp5 = plt.subplot(4, 3, 5)
sp6 = plt.subplot(4, 3, 6)
sp7 = plt.subplot(4, 3, 7)
sp8 = plt.subplot(4, 3, 8)
sp9 = plt.subplot(4, 3, 9)
sp10 = plt.subplot(4, 3, 10)
sp11 = plt.subplot(4, 3, 11)
sp12 = plt.subplot(4, 3, 12)

# get the iris dataset
iris = load_iris()

# store the data from the set as a numpy array object called 'data'
data = np.array(iris['data'])

# store the classes of each observation in the dataset (0, 1, 2) as 'targets'
targets = np.array(iris['target'])

# give each class a colour and store as dictionary
cd = {0: "r", 1: "b", 2: "g"}

# apply the colours to each of the classes in the targets array
cols = np.array([cd[target] for target in targets])

# make the scatter plots with @Param as x values, y values, the colours
# x values as sepal length (first element of each row in data)
# y values are sepal width
sp1.scatter(data[:, 0], data[:, 1], c=cols)
# y values are petal length
sp2.scatter(data[:, 0], data[: ,2], c=cols)
# y values are petal width
sp3.scatter(data[:, 0], data[: ,3], c=cols)

# x values as sepal width (second element)
# y values are 0, 2, 3, sepal length, petal length, petal width respectively
sp4.scatter(data[:, 1], data[: ,0], c=cols)
sp5.scatter(data[:, 1], data[: ,2], c=cols)
sp6.scatter(data[:, 1], data[: ,3], c=cols)

# x values as petal length (third element)
# y values are 0, 1, 3, sepal length, sepal width and petal width respectively
sp7.scatter(data[:, 2], data[: ,0], c=cols)
sp8.scatter(data[:, 2], data[: ,1], c=cols)
sp9.scatter(data[:, 2], data[: ,3], c=cols)

# x values as petal width (fourth element)
# y values are 0, 1, 2, sepal length, sepal width and petal length respectively
sp10.scatter(data[:, 3], data[: ,0], c=cols)
sp11.scatter(data[:, 3], data[: ,1], c=cols)
sp12.scatter(data[:, 3], data[: ,2], c=cols)

# display the figure
plt.show()
