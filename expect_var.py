#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar


filename1 = sys.argv[1]

data1 = np.loadtxt(filename1,  delimiter=',')

t = np.arange(0, 1000.0, 1)

a=0.5
b=0.5
fun = t*(a+b)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
#ax1.plot(data1[:,0],data1[:,1],color="black",label=r'$E$')
ax1.plot(data1[:,0],data1[:,2],color="black",label='numerical')
ax1.plot(t, fun, color="red", label='analitycal')
plt.grid()
plt.legend(loc="upper left", fontsize=18)

plt.ylabel(r'$\sigma^2$', fontsize=24)
plt.xlabel(r'$t$', fontsize=24)


axins = zoomed_inset_axes(ax1, 60, loc=4) # zoom = 0.5

axins.plot(data1[:,0],data1[:,2],color="black")
axins.plot(t, fun, color="red")
#plt.grid()
axins.annotate('x60', xy=(1, 1), xycoords='axes fraction',
            size=14, ha='right', va='top',
            bbox=dict(boxstyle='round', fc='w'))
x1, x2, y1, y2 = 810, 820, 810, 820 # specify the limits
axins.set_xlim(x1, x2) # apply the x-limits
axins.set_ylim(y1, y2) # apply the y-limits

plt.xticks(visible=False)
plt.yticks(visible=False)

from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mark_inset(ax1, axins, loc1=2, loc2=4, fc="none", ec="0.5")




plt.draw()
#plt.show()
plt.savefig("0505variance.pdf")

