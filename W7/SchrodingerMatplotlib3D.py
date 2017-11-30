import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.load('xdata300.dat')
y = np.load('ydata300.dat')
z = np.load('zdata300.dat')
mag = np.load('density300.dat')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for a in range(0, len(mag)):
    for b in range(0, len(mag)):
        for c in range(0, len(mag)):
            ax.scatter(x[a][b][c], y[a][b][c], z[a][b][c], marker='o', alpha=(mag[a][b][c] / np.amax(mag)))
plt.show()
