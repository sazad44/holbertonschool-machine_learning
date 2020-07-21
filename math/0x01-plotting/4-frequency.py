#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
a, b, c = plt.hist(student_grades, edgecolor='black', linewidth=1.6, range=(0, 100), color='#0082b7')
plt.margins(0)
plt.ylim(0, 30)
plt.xticks(b)
plt.show()
