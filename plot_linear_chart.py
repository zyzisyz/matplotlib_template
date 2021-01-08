#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

# x and y data
x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# plot X and Y
plt.plot(x, y_sin, label="sin")
plt.plot(x, y_cos, label="cos")

# plot X and Y axis label
plt.xlabel("x axis label")
plt.ylabel("y axis label")

# plot title
plt.title("Sine and Cosine")

# plt legend and grid
plt.legend()
plt.grid()


# plt show and save
plt.show()
plt.savefig("linear_chart.png")

