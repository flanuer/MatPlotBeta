#!/usr/bin/python
# Python script to run matplotlib 12/12/2019

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()