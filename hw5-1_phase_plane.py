import numpy as np
import matplotlib.pyplot as plt
#
# du/dt = u * Da / (1 + u * s)**2 - 1

duf = lambda u, Da, s: u * Da / (1 + u * s) ** 2 - 1
dt = 0.01
times = list(np.arange(0, 1, dt))
concentrations = []
uold = 0.0  # Initial Condition
u = uold
Da = 4.0
s = 0.6
for t in times:
    u = uold + duf(u, Da, s) * dt
    concentrations.append(u)
    uold = u

plt.plot(times, concentrations)
plt.show()
