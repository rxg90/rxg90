# -*- coding: utf-8 -*-
#%% Importar librerias

import random
import numpy as np
import matplotlib.pyplot as plt

#%% 5.10 Crear
def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album

#%% 5.11 Incompleto
    
def album_incompleto(A):
    if all(a>=1 for a in A):
        return True
    else:
        return False

#%% 5.12 Comprar
        
def comprar_figu(figus_total):
    figu=random.randint(1,figus_total)
    return figu

#%% 5.13 Cantidad de compras
#figus_total = 670
def cuantas_figus(figus_total):
    A = crear_album(figus_total)
    album_incompleto(A)
    CantFigus=0
    while album_incompleto(A)== False:
        #for i,a in enumerate(A):
       figu = comprar_figu(figus_total) 
       A[figu-1] +=1
       CantFigus +=1
       #print(A)
       album_incompleto(A)
    return CantFigus

#%%  5.15 
#n_repeticiones=1000
#figus_total=6
def experimento_figus(n_repeticiones,figus_total):
    i=0
    l=[]
    while i<n_repeticiones:
        total_figus=cuantas_figus(figus_total)
        l.append(total_figus)
        i +=1
    figus_promedio=np.mean(l)
    #print(l)
    #print(figus_promedio)
    return figus_promedio
        
#%% 5.17     
           
def comprar_paquete(figus_total, figus_paquete):
    paquete=[]
    for p in range(figus_paquete):
        paquete.append(random.randint(1,figus_total))
    return paquete           

#%% 5.18
    
def cuantos_paquetes(figus_total, figus_paquete):
    A = crear_album(figus_total)
    album_incompleto(A)
    CantPaquetes=0
    while album_incompleto(A)== False:
        for c in comprar_paquete(figus_total, figus_paquete):
           figu = c
           #print(figu)
           A[figu-1] +=1
        CantPaquetes +=1
       #print(A)
        album_incompleto(A)
    return CantPaquetes

#%% 5.19
    

def experimento_paquetes(n_repeticiones,figus_total,figus_paquete):
    i=0
    l=[]
    while i<n_repeticiones:
        total_paquetes=cuantos_paquetes(figus_total,figus_paquete)
        l.append(total_paquetes)
        i +=1
    paquetes_promedio=np.mean(l)
    #print(l)
    #print(figus_promedio)
    return paquetes_promedio

#%% Graficar el llenado del album
    
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    #print(album)
    historia_figus_pegadas = [0]
    while album_incompleto(album)== False:
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        #print(figus_pegadas)
        historia_figus_pegadas.append(figus_pegadas)
        #print(historia_figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()