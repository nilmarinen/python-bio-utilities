import matplotlib.pyplot as plt
import numpy as np
x = np.array([0.0000, 0.0005, 0.005, 0.015, 0.05, 0.15, 0.5, 1.5, 5, 15, 50, 500, 5000, 50000])
y = np.array([2544.6, 2707.0, 2763.3, 2886.0, 4379.3, 7752.0, 18483.0, 32010.7, 44210.7, 52790.0, 51278.3, 51188.3, 55787.0, 57780.7])

plt.plot(x, y)
plt.xscale('log')
plt.show()
