import numpy as np
import matplotlib.pyplot as plt
from sys import exit

Ns = 100
Nu = 100
smin = 0.01
smax = 10
umin = 0.01
umax = 10.03

sl = list(np.arange(smin, smax, (smax - smin) / Ns))
ul = list(np.arange(umin, umax, (umax - umin) / Nu))

Daf = lambda u, s: (1 + u * s) ** 3 / (2 * u * s - 1 - u * s)

fig1 = plt.figure(1, figsize=(12, 6))

for (i, s) in enumerate(sl):
    for (j, u) in enumerate(ul):
        Da[i, j] = Daf(u, s)


ax1 = fig1.add_subplot(1, 2, 2)
#ax1.imshow(Da, interpolation='nearest')
x, y = np.mgrid[0:Ns, 0:Nu]
CS = ax1.contour(y, x, Da)
ax1.set_xlabel(r'$\sigma = K C_f$')
ax1.set_ylabel(r'$u = C / C_f$')
ax1.set_title(r'$Da = k \theta = k V / q$')

ax2 = fig1.add_subplot(1, 2, 1)

urange = list(np.arange(2.5, 12.5, 2.5))
urange.append(0.1)
urange.sort()
for u in urange:
    Dal = []
    for s in sl:
        Dal.append(Daf(u, s))
    ax2.plot(sl, Dal)
ax2.set_xlabel(r'$s$')
ax2.set_ylabel(r'$Da$')
ax2.legend([r'$u = %.1f$'%u for u in urange], loc='best')
ax2.set_title(r'Steady state curves in the $(\sigma, Da)$ space for various $u$')
plt.suptitle('Hw5')
#ax3 = fig1.add_subplot(1, 3, 3)
#Dal = []
#u = -5.0
#for s in sl:
#    Dal.append(Daf(u, s))
#ax3.plot(sl, Dal)
#ax3.set_xlabel(r'$s$')
#ax3.set_ylabel(r'$Da$')
#ax3.set_title(r'$u = -5$')

plt.clabel(CS, inline=1, fontsize=10)

plt.tight_layout(pad=1.2, h_pad=None, w_pad=None)
#plt.savefig('hw5_1a.pdf')
plt.show()
