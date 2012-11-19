import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

tmin = 0.0
tmax = 2 * pi
dt = 0.01

tl = list(np.arange(tmin, tmax, dt))
xl = [np.cos(t) for t in tl]
yl = [np.sin(t) for t in tl]

fig = plt.figure(1, figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.plot(tl, xl, label=r'$x=cos(t)$')
ax1.plot(tl, yl, label=r'$y=sin(t)$')
ax2.plot(xl, yl, label=r'$y$ vs $x$')

ax1.set_xlim((tmin, tmax))
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y$')
ax1.set_title('Dafuq is this?')
ax2.set_title('It\'s a circle, dumpass.')

fig.suptitle('Parametric Plots are good, M\'kay?')
ax1.legend()
plt.savefig('parametric.png')
plt.show()
