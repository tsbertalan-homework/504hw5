import matplotlib.pyplot as plt
from sys import exit
import numpy as np
from finder import findroots
from characterizer import findCharacter, eigenvalues
f = lambda y, g: np.exp(y / (1 + y / g))
dyf = lambda y, a, b, g: f(y, g) * (a * b * g - a * y) - y
dxf = lambda y, a, b, g: dyf(y, a, b, g) / b / g

start = 0.1
stop = 50
resolution = 10000
yl = list(np.arange(start, stop, (stop - start) / resolution))
a = 0.004
b = 4
g = 12

labelx = r'concentration rate-of-change, $dx/d\tau$'
labely = r'temperature rate-of-change, $dy/d\tau$'
dxl = [dxf(y, a, b, g) for y in yl]
dyl = [dyf(y, a, b, g) for y in yl]

fig = plt.figure(1, figsize=(11, 8.5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(yl, dxl, 'k--', label=labelx)
ax.plot(yl, dyl, 'k-', label=labely)
roots = findroots(yl, dyl)
print 'roots are', roots
print 'roots / e are', [root / np.exp(1) for root in roots]
ax.scatter(roots, [0]*len(roots))


for root in roots:
    x = root / b / b
    y = root
    print 'At (%.3f, %.3f)' % (x, y)
    annotation = r'$y_s=%.3f$' % root + '\n' + findCharacter(x, y, a, b, g)
    ax.annotate(annotation, xy=(root, 0), xytext=(1.1*root, -0.4))
    print 'eigenvalues are', eigenvalues(x, y, a, b, g)
    print 'this steady-state is:', findCharacter(x, y, a, b, g)
ax.axhline(color='black')
ax.set_xlabel(r'$y$')
ax.set_ylabel(r'$dy/d\tau$ or $dx/d\tau$')
#ax.set_xlim((0, 5.2))
ax.set_ylim((-1.5, 1.5))
ax.set_xscale('log')
ax.legend(loc='upper left')
fig.suptitle('CBE 504 HW 5, Part 2: Multiple CSTR Steady States \n Tom Bertalan \n'\
          + r'$\alpha=%.3f$, $\beta=%.0f$, $\gamma=%.0f$' % (a, b, g))
fig.savefig('hw5_2.pdf')
#plt.show()
