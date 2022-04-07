import matplotlib.pyplot as plt
import numpy as np

from data import data, date

x = range(len(data))

print(np.average(data)/60)

plt.plot(x, data)
plt.grid()
plt.xlabel('Index')
plt.ylabel('Reply Time [min]')
plt.title(f'Record Reply Time - {date}')
plt.show()

