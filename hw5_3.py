import numpy as np
from scipy import sqrt
import matplotlib.pylab as plt
start = 0.1
stop = 45
resolution = 10000
bl = list(np.arange(start, stop, (stop - start) / resolution))
g = 4*(1 + 1 / min(bl)) + 0.1
xf = lambda b: (b*(g - 2) + sqrt((2*b-g*b)**2 - 4*b*(b+g))) / (b*2*(b+g))
yf = lambda b, x: b * g * x
af = lambda x, y, g: x / (1 - x) * np.exp((1 + y / g) / y)

xl = []
yl = []
al = []
for b in bl:
    x = xf(b)
    y = yf(b, x)
    a = af(x, y, g)
    if a > 0 and b > 0 and g > 0 and y > 0:
        xl.append(x)
        yl.append(y)
        al.append(a)
fig = plt.figure(figsize=(11, 8.5))
ax1 = fig.add_subplot(1, 2, 1)  # for b
ax2 = fig.add_subplot(1, 2, 2)  # for ln(b)
ax1.plot(al, bl, 'k')
logbl = [np.log(b) for b in bl]
ax2.plot(al, logbl, 'k')
ax1.set_xlabel(r'$\alpha$')
ax2.set_xlabel(r'$\alpha$')
ax1.set_ylabel(r'$\beta$')
ax2.set_ylabel(r'$ln(\beta)$')
zeros = [0 for b in bl]
ax1.fill_betweenx(bl, zeros, al, alpha=0.2, facecolor='black')
ax2.fill_betweenx(logbl, zeros, al, alpha=0.2, facecolor='black')
ax2.set_ylim((min(logbl), 3))
ax1.set_xlim((0, max(al)))
ax2.set_xlim((0, max(al)))
#ax1.set_yscale('log')
#plt.xscale('log')
fig.suptitle('CBE 504 HW5 Part 3 \n Tom Bertalan \n' + r'$\gamma = %.3f$' % g)
#plt.tight_layout(pad=1.2, h_pad=None, w_pad=None)
fig.savefig('hw5_3.pdf')
#plt.show()
