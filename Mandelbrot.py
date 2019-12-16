import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch

xmin = -2
xmax = 1
ymin = -1
ymax = 1


pts = 250

x = np.linspace(xmin,xmax,pts)
y = np.linspace(ymin,ymax,pts)

xx,yy = np.meshgrid(x,y)

@np.vectorize
def calc_val(re, im):
    # assume 100 tries per spot
    z_now = np.complex(0,0)
    z_next = np.complex(0,0)
    p = np.complex(re,im)
    for i in range(100):
        z_now = z_next
        z_next = np.multiply(z_now,z_now) +p
        if np.absolute(z_next) >=2:
            return 1

    if np.absolute(z_next) < 2:
        return 0
    else:
        return i

Z = calc_val(xx,yy)


fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
               origin='lower', extent=[xmin, xmax, ymin, ymax],
               vmax=1, vmin=0)

plt.show()