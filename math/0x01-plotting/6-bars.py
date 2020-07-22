#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

i = 0
people = ['Farrah', 'Fred', 'Felicia']
colors = ['red', 'yellow', 'orange', '#ffe5b4']
for person in range(len(people)):
    b = 0
    for f in range(len(fruit)):
        plt.bar(
            people[person],
            fruit[f][person],
            color=colors[f],
            bottom=b,
            width=0.5
        )
        b += fruit[f][person]
plt.ylim(0, 80)
plt.legend(('apples', 'bananas', 'oranges', 'peaches'))
plt.title('Number of Fruit per Person')
plt.ylabel('Quantity of Fruit')
plt.show()
