from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

from data import data, date


param = norm.fit(data)

x = np.arange(0, 3600, 0.01)

y = norm.pdf(x, param[0], param[1])

plt.plot(x, y)
plt.title(f'Gaussian Fitting - {date}')
plt.xlabel('Reply Time [min]')
plt.ylabel('Probability')
plt.grid()
plt.show()
