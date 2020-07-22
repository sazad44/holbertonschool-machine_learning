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
fig.suptitle("All in One")
fig.tight_layout(pad=2.2)
ax[0, 0].plot(y0, color='red')
ax[0, 0].set_ylim(0, 1000)
ax[0, 0].set_xlim(0, 10)
ax[0, 1].scatter(x1, y1, color='#c82dbf', marker='.')
ax[0, 1].set_title("Men's Height vs Weight", fontsize='x-small')
ax[0, 1].set_xlabel("Height (in)", fontsize='x-small')
ax[0, 1].set_ylabel("Weight (lbs)", fontsize='x-small')
ax[1, 0].plot(x2, y2, color='#0082b7')
ax[1, 0].set_yscale('log')
ax[1, 0].set_xlim(0, 28650)
ax[1, 0].set_title("Exponential Decay of C-14", fontsize='x-small')
ax[1, 0].set_xlabel('Time (years)', fontsize='x-small')
ax[1, 0].set_ylabel('Fraction Remaining', fontsize='x-small')
ax[1, 1].plot(x3, y31, 'r--')
ax[1, 1].plot(x3, y32, 'g')
ax[1, 1].set_title(
    'Exponential Decay of Radioactive Elements',
    fontsize='x-small'
)
ax[1, 1].set_ylim(0, 1)
ax[1, 1].set_xlim(0, 20000)
ax[1, 1].legend(('C-14', 'Ra-226'), fontsize='x-small')
ax[1, 1].set_xlabel('Time (years)', fontsize='x-small')
ax[1, 1].set_ylabel('Fraction Remaining', fontsize='x-small')
plt.subplot(313)
a, b, c = plt.hist(
    student_grades,
    edgecolor='black',
    linewidth=1.6,
    range=(0, 100),
    color='#0082b7'
)
plt.margins(0)
plt.ylim(0, 30)
plt.xticks(b)
plt.title('Project A', fontsize='x-small')
plt.xlabel('Grades', fontsize='x-small')
plt.ylabel('Number of Students', fontsize='x-small')
plt.show()
