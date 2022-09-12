# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:10:55 2021

@author: rxgfilo
"""

import comparaciones_ordenamiento as co
import numpy as np
import timeit as tt
import matplotlib.pyplot as plt
"""
def generar_lista(N):
    lista = [0]  * N
    for i in range(N):
      lista[i] = random.randint(1, 1000)
    return lista

"""
def experimento_timeit(Nmax):
    tiempos_seleccion=[]
    tiempos_insercion=[]
    tiempos_burbujeo=[]
    tiempos_merge=[]
    largo_lista=[]
    #Nmax=100
    for i  in range(Nmax):
        lista=co.generar_lista(i)#genera lista incremental
        largo_lista.append(i)
        #print(lista)
        tiempo_seleccion = tt.timeit('co.ord_seleccion(lista.copy())', number = Nmax,globals = globals())
        tiempo_insercion = tt.timeit('co.ord_insercion(lista.copy())', number = Nmax,globals = globals())
        tiempo_burbujeo = tt.timeit('co.ord_burbujeo(lista.copy())', number = Nmax,globals = globals())
        tiempo_burbujeo = tt.timeit('co.ord_burbujeo(lista.copy())', number = Nmax,globals = globals())
        tiempo_merge = tt.timeit('co.merge_sort(lista.copy())', number = Nmax,globals = globals())
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_seleccion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_merge.append(tiempo_merge)
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    largo_lista=np.array(largo_lista)
    #print(tiempos_seleccion,largo_lista)
    plt.plot(largo_lista, tiempos_seleccion,c = 'blue')
    plt.plot(largo_lista, tiempos_insercion,linestyle='dotted',c = 'red')
    plt.plot(largo_lista, tiempos_burbujeo,c = 'green')
    plt.plot(largo_lista, tiempos_merge,c = 'grey')
    
    
#experimento_timeit(100)