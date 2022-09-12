# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:10:25 2021

@author: rxgfilo
"""
#Importo liberiras
import numpy as np
import matplotlib.pyplot as plt


#%% defino funcion

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

#%%
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])


g = plt.scatter(x = superficie, y = alquiler)
plt.title('precio_alquiler ~ superficie')
#plt.plot(alquiler, superficie)
plt.xlabel('superficie')
plt.ylabel('alquiler')

plt.show()
#%%Ajuste

a,b= ajuste_lineal_simple(superficie,alquiler)

grilla_x = np.linspace(start = minx, stop = maxx, num = 200)
grilla_y = grilla_x*a + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

#%% Error Cuadratico Medio

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())