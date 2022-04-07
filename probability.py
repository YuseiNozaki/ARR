from scipy.stats import norm
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

from data import data, date


start = 0
end = 1440
step = 0.01

x = np.arange(0, 4000, step)

y = np.zeros(len(x))

for d in tqdm(data):
    fx = np.array(norm.pdf(x, d, 100))
    y += fx

y *= 100/(sum(y)*step)

prob = sum(y[int(start/step) : int(end/step)]) * step

print(f'{start}min ~ {end}min : {int(prob)}%')

plt.plot(x, y)
plt.title(f'Probability Distribution of Reply Time - {date}')
plt.xlabel('Reply Time [min]')
plt.ylabel('Probability [%]')
plt.grid()
plt.show()
