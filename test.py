import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

y1 = np.cos(x)

plt.scatter(x, y ,c='black', marker='.')
plt.scatter(x, y1 ,c='red', marker='.')
plt.show()