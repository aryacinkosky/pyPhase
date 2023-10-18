# Phase Space of a Dynamic System

import matplotlib.pyplot as plt
import math

a = 1
b = 3
dt = 0.01 

x = 1
y = 1 

r = 10000 # range

x_values = [x]  # Start with the initial value of x
y_values = [y]  # Start with the initial value of y

for i in range(r):
    dx = (a + (x * x * y) - b * x - x) * dt
    dy = (b * x - (x * x) * y) * dt

    x += dx
    y += dy

    x_values.append(x)
    y_values.append(y)

plt.figure(figsize=(8, 6))
plt.scatter([i * dt for i in range(r + 1)], x_values, s=1, c='b', marker='o', label='x')
plt.scatter([i * dt for i in range(r + 1)], y_values, s=1, c='r', marker='o', label='y')
plt.title('Graph of x and y in terms of dt')
plt.xlabel('t (time)')
plt.ylabel('x and y')
plt.legend()
plt.grid(True)
plt.show()