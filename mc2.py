from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt


digits = load_digits()

print(digits.keys())

n_samples, n_features = digits.data.shape

print(n_samples, n_features)

# print(digits.data[0])


# print(digits.target)

print(digits.data.shape)
print(digits.images.shape)

print(np.all(digits.images.reshape((1797, 64)) == digits.data))

print(digits.data.__array_interface__['data'])
print(digits.images.__array_interface__['data'])


# set up the figure
fig = plt.figure(figsize=(6, 6))  # figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# plot the digits: each image is 8x8 pixels
for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

    # label the image with the target value
    ax.text(0, 7, str(digits.target[i]))

plt.show()
