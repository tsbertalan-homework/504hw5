import matplotlib.pylab as plt
import numpy as np
from scipy import sqrt

start = 0.042
stop = 0.450
resolution = 10070
ul = list(np.arange(start, stop, (stop - start) / resolution))
ul1 = list(np.arange(start, 0.249, (0.249 - start) / resolution))
ul2 = list(np.arange(0.251, stop, (stop - 0.251) / resolution))
sf = lambda u: 1 / u / (1 - 2 * u)
Daf = lambda u: (1 - u) / u * (u * sf(u) + 1) ** 2
sl = [sf(u) for u in ul]
Dal = [Daf(u) for u in ul]

sl1 = [sf(u) for u in ul1]
Dal1 = [Daf(u) for u in ul1]

sl2 = [sf(u) for u in ul2]
Dal2 = [Daf(u) for u in ul2]

fig = plt.figure(1, figsize=(11, 8.5))
ax = fig.add_subplot(1, 1, 1)

ax.plot(sl, Dal, 'k')
ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$Da$')
#ax.yscale('log')
#ax.xscale('log')
print 'minimum s is', min(sl)
print 'minimum Da is', min(Dal)
def uf(s):
    disc = 1.0 - 8.0 / s
    return ((-1 + sqrt(disc)) / 2, (-1 - sqrt(disc)) / -4.0)
print 'u there is probably one of these:', uf(min(sl))

xvertices = []
yvertices = []

xvertices.extend(sl2)  # left edge
yvertices.extend(Dal2)

yvertices.append(max(Dal))  # top
xindex = Dal.index(max(Dal))
xvertices.append(sl[xindex])

xvertices.append(max(sl))  # right
yindex = sl.index(max(sl))
yvertices.append(Dal[yindex])

xvertices.append(min(sl))  # bottom
yvertices.append(min(Dal))

ax.fill(xvertices, yvertices, alpha=0.2, facecolor='black')

ax.set_xlim((5, sl[xindex]))
ax.set_ylim((20, Dal[yindex]))

def eigenvalue(Da, s, u):
    return 2 * Da * s * u / (s * u + 1) ** 3 - Da / (s * u + 1) ** 2 - 1

l = eigenvalue(60, 15, max(uf(15)))
print 'eigenvalue is', l

ax.scatter([15], [60], color='black')
annotation = r'$u = %.3f$' % max(uf(15)) + '\n'\
     + r'$\lambda = %.3f$' % l
ax.annotate(annotation, xy=(15, 60), xytext=(14.5, 63.5))

fig.suptitle('CBE 504 HW5, Part 1 \n Tom Bertalan')
fig.savefig('hw5_1.pdf')

#ax.show()
