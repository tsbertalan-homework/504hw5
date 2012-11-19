import matplotlib.pyplot as plt
import numpy as np
Sf = lambda y,g: y / (1 + y / g)
dyf = lambda y, a, b, g: -y + np.exp(Sf(y,g)) * (a * b * g - a * y)
dxf = lambda y, a, b, g: dyf(y, a, b, g) / b / g
ddyf = lambda y, a, b, g: (a*b*g - a*y)*(g*(y/g+1)+y)/g/(y/g+1)*np.exp(Sf(y,g)) - a*np.exp(Sf(y,g))  -1
J0condf = lambda x, a, b, g: -b*g*x**2 + b*g*x - 1

yl = list(np.arange(0,1,.01))
a = 1.5
b = 0.0
g = 1.5
trial_values = [1, 3]
maxinit = 0
maxparams = (0, 0, 0)

#for a in trial_values:
for b in trial_values:
    for g in trial_values:
        label = r'$\alpha=%i$, $\beta=%i$, $\gamma=%i$'%(a,b,g)
        dxl = [dxf(y, a, b, g) for y in yl]
        ddyl = [ddyf(y,a,b,g) for y in yl]
        dyl = [dyf(y, a, b, g) for y in yl]
        j0condl = [J0condf(x, a, b, g) for x in yl]
        plt.plot(yl, dyl, label=label)
        if dyl[0] > maxinit:
            maxinit = dyl[0]
            maxparams = (a, b, g)
        if ddyl[0] > 0 and dyl[0] == 0:
            print 'ddyl[0] =', ddyl[0], '> 0', 'for (a b g) = (', a,b,g, ')'
        absdyl = [abs(dy) for dy in dyl]
        zeroest = min(absdyl)
        ys = yl[absdyl.index(zeroest)]
        print 'ys =', ys, 'for', a, b, g
print 'highest initial rate was', maxinit, 'at', a, b, g
plt.axhline(color='black')
plt.legend()
plt.show()
