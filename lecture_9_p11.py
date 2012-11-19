import numpy as np
import matplotlib.pyplot as plt

lf = lambda(ys): (ys - 1) / np.exp(ys)
muf = lambda(ys): ys * lf(ys)

ysmin = 1
ysmax = 10
dys = 0.1

ysl = list(np.arange(ysmin, ysmax, dys))
ll = [lf(ys) for ys in ysl]
mul = [muf(ys) for ys in ysl]

fig = plt.figure(1, figsize=(11, 8.5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(mul, ll)
ax.set_xlabel(r'$\mu(y_s) = y_s \lambda(y_s)$')
ax.set_ylabel(r'$\lambda(y_s) = (y_s - 1) / e^{y_s}$')
ax.set_title('Lecture 9, Slide 11 \n' + r' $y_s$ ranges from %i to %i' % (ysmin, ysmax))
plt.savefig('lecture_9_p11.png')
plt.show()
