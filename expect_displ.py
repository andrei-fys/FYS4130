#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

filename1 = sys.argv[1]

data1 = np.loadtxt(filename1,  delimiter=',')
t = np.arange(0, 1000.0, 1)

a=0.5
b=0.5
fun = t*(a-b)
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(data1[:,0],data1[:,1],color="black",label='numerical')
ax1.plot(t, fun, color="red", label='analitycal')
#ax1.plot(data1[:,0],data1[:,2],color="red",label=r'$E$')
plt.grid()


#ax1.set_ylim([-300,100])
plt.legend(loc="upper right", fontsize=18)

plt.xlabel(r'$t$', fontsize=24)
plt.ylabel(r'$\langle n\rangle$', fontsize=24)

plt.draw()
#plt.show()
plt.savefig("0505displacement.pdf")


