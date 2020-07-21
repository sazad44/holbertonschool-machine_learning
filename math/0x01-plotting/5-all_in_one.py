#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig, ax = plt.subplots(3, 2)
plt.title("All in One")
ax[0, 0].plot(y0, color='red')
plt.ylim(0, 1000)
plt.xlim(0, 10)
ax[0, 1].scatter(x1, y1, color='magenta', marker='.')
plt.title("Men's Height vs Weight")
plt.xlabel("Height (in)")
plt.ylabel("Weight (lbs)")
ax[1, 0].plot(x2, y2, color='#0082b7')
plt.yscale('log')
plt.xlim(0, 28650)
plt.title("Exponential Decay of C-14")
ax[1, 1].plot(x3, y31)
plt.subplot(313)
plt.plot(x3, y32)
plt.show()
