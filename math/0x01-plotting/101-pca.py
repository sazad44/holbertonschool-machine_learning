#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

fig = plt.figure()
ax = Axes3D(fig)
cm = plt.cm.get_cmap('plasma')
xy = [pca_data[i][0] for i in range(len(pca_data))]
xs = [pca_data[i][1] for i in range(len(pca_data))]
ys = [pca_data[i][2] for i in range(len(pca_data))]
ax.scatter(xy, xs, ys, c=labels, cmap='plasma')
plt.title('PCA of Iris Dataset')
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')
plt.show()
