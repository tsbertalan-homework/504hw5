import matplotlib.pyplot as plt
import numpy as np
from finder import findroots
from characterizer import findCharacter, eigenvalues
f = lambda y, g: np.exp(y / (1 + y / g))
dyf = lambda y, a, b, g: f(y, g) * (a * b * g - a * y) - y
dxf = lambda y, a, b, g: dyf(y, a, b, g) / b / g

yl = list(np.arange(0, 6, 0.004))
a = 0.004
b = 4
g = 12

labelx = r'concentration rate-of-change, $dx/d\tau$'
labely = r'temperature rate-of-change, $dy/d\tau$'
dxl = [dxf(y, a, b, g) for y in yl]
dyl = [dyf(y, a, b, g) for y in yl]

plt.plot(yl, dxl, 'k--', label=labelx)
plt.plot(yl, dyl, 'k-', label=labely)
roots = findroots(yl, dyl)
print 'roots are', roots
plt.scatter(roots, [0]*len(roots))


for root in roots:
    x = root / b / b
    y = root
    print 'At (%.3f, %.3f)' % (x, y)
    annotation = r'$y_s=%.3f$' % root + '\n' + findCharacter(x, y, a, b, g)
    plt.annotate(annotation, xy=(root, 0), xytext=(root, -0.4))
    print 'eigenvalues are,', eigenvalues(x, y, a, b, g)
    print 'this steady-state is:', findCharacter(x, y, a, b, g)
plt.axhline(color='black')
plt.xlabel(r'$y$')
plt.ylabel(r'$dy/d\tau$ or $dx/d\tau$')
plt.xlim((0, 5.2))
plt.ylim((-1.5, 1.5))
plt.yscale('log')
plt.legend()
plt.title('Multiple CSTR Steady States \n'\
          + r'$\alpha=%.3f$, $\beta=%.0f$, $\gamma=%.0f$' % (a, b, g))
plt.show()
