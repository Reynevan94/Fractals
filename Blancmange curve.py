import matplotlib.pyplot as plt
import numpy as np


A = 1  # height of first triangle
yfin = []  # list of sections
pts = 100  # number of points
X = range(pts)  # x domain, high  value gives better resolution
P = pts/2
steps = 20  # number of iterations

for j in range(steps):
    x = 0
    y = []
    for x in X:
        y.append((A/P) * (P - abs(x % (2*P) - P)))  # generating triangle signal on x domain
    P = P/2
    A = A/2
    yfin.append(y)


xdomain = list(map(lambda x: x/pts, list(X))) # normalisation of domain to 1
ySum = np.sum(yfin, axis=0)
plt.plot(xdomain,ySum)
plt.show()
