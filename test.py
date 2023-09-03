import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

plt.scatter(x, y ,c='black', marker='.')
plt.show()