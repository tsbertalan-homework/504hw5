import numpy as np
import matplotlib.pylab as plt
start = 0.01
stop = 4
resolution = 10000
xl = list(np.arange(start, stop, (stop - start) / resolution))
bf = lambda x: 1 / x - 2
gf = lambda b: 4*(1 + 1 / b)
yf = lambda b, g, x: b * g * x
af = lambda x, y, g: x / (1 - x) * np.exp((1 + y / g) / y)

bl = []
gl = []
yl = []
al = []
for x in xl:
    b = bf(x)
    g = gf(b)
    y = yf(b, g, x)
    a = af(x, y, g)
    if a > 0 and b > 0 and g > 0 and y > 0:
        print 'b', b, 'g', g, 'y', y, 'a', a
        bl.append(b)
        gl.append(g)
        yl.append(y)
        al.append(a)
print max(gl)
plt.plot(al, bl)
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\beta$')
plt.show()
