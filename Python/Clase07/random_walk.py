# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:42:06 2021

@author: rxgfilo
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
"""
plt.plot(randomwalk(N),color="blue", linewidth=0.5)
plt.plot(randomwalk(N),color="red", linewidth=0.5)
plt.plot(randomwalk(N),color="yellow", linewidth=0.5)
plt.plot(randomwalk(N),color="green", linewidth=0.5)
plt.plot(randomwalk(N),color="gray", linewidth=0.5)
plt.plot(randomwalk(N),color="violet")
plt.plot(randomwalk(N),color="black")
plt.plot(randomwalk(N),color="orange")
plt.plot(randomwalk(N),color="brown")
plt.plot(randomwalk(N),color="purple")
plt.plot(randomwalk(N),color="magenta")
plt.plot(randomwalk(N),color="cyan")
#plt.plot(randomwalk(N),color='#1f77b4')
plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.show()
"""

#%%

fig = plt.figure()
plt.subplot(2, 1, 1)
plt.plot(randomwalk(N),color="blue", linewidth=0.5)
plt.plot(randomwalk(N),color="red", linewidth=0.5)
plt.plot(randomwalk(N),color="yellow", linewidth=0.5)
plt.plot(randomwalk(N),color="green", linewidth=0.5)
plt.plot(randomwalk(N),color="gray", linewidth=0.5)
plt.plot(randomwalk(N),color="violet")
plt.plot(randomwalk(N),color="black")
plt.plot(randomwalk(N),color="orange")
plt.plot(randomwalk(N),color="brown")
plt.plot(randomwalk(N),color="purple")
plt.plot(randomwalk(N),color="magenta")
plt.plot(randomwalk(N),color="cyan")
#plt.plot(randomwalk(N),color='#1f77b4')
plt.title("Caminatas al azar")
#plt.xlabel("Tiempo")
#plt.ylabel("Distancia al origen")
plt.xticks([]), plt.yticks([]) # saca las marcas


plt.subplot(2, 2, 3)
plt.plot(randomwalk(N),color="green", linewidth=0.5)
plt.title("La caminata que mas se aleja",fontsize=10)


plt.subplot(2, 2, 4)
plt.plot(randomwalk(N),color="green", linewidth=0.5)
plt.title("La caminata que menos se aleja",fontsize=10)

plt.show()
