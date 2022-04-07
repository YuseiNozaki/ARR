from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from data import data, date


step = 0.01

x = np.arange(0, 4000, step)

y = np.zeros(len(x))

for d in tqdm(data):
    fx = np.array(norm.pdf(x, d, 100))
    y += fx


y *= 100/(sum(y)*step)


plt.plot(x, y)
plt.title(f'Probability Distribution of Reply Time - {date}')
plt.xlabel('Reply Time [min]')
plt.ylabel('Probability [%]')
plt.grid()
plt.show()
