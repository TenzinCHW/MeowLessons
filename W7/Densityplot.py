# Another pretty 3D plot
import numpy as np
from mayavi import mlab

x = np.load('xdata210.dat')
y = np.load('ydata210.dat')
z = np.load('zdata210.dat')
density = np.load('density210.dat')
figure = mlab.figure('DensityPlot')
mag = density / np.amax(density)
pts = mlab.points3d(mag, opacity=0.5, transparent=True)  # This is to plot the magnitude
mlab.colorbar(orientation='vertical')
mlab.axes()
mlab.show()
