import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import numpy as np
import sklearn
from sklearn.datasets import make_moons

def f(X, Y, mean, cov):
    d = np.dstack([X, Y])
    gaussian = multivariate_normal(mean = mean, cov = cov)
    return gaussian.pdf(d)

mean = [2.5, 2.5]
cov = [[1.0, 0.0], [0.0, 1.0]]

x = np.linspace(0, 5, 1000)
y = np.linspace(0, 5, 1000)
X, Y = np.meshgrid(x, y)
Z = f(X, Y, mean, cov)

plt.imshow(Z)

plt.pcolormesh(X, Y, Z, cmap='RdBu')
plt.colorbar()
plt.show()

