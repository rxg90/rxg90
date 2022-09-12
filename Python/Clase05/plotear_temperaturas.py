# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#def plotear_temperaturas():
temperaturas=np.load('temperaturas.npy')
plt.hist(temperaturas,bins=30)
plt.show()

