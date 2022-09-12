#%% Importar librerias

import csv 
import os
import matplotlib.pyplot as plt
import numpy as np


#%% Ejercicio 4.15: Lectura de todos los √°rboles

def leer_arboles(nombre_archivo):
    arboleda=[]
    with open(nombre_archivo,'rt',encoding="utf8") as f:
        rows=csv.reader(f)
        headers= next(rows)
        for nrow,row in enumerate(rows):
            record=dict(zip(headers,row))
            arboleda.append(record)
        return arboleda
            
    

#%% 4.16 Lista de altos de jacaranda

arboleda= leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
#print(arboleda)

h=[float(arbol['altura_tot'])for arbol in arboleda if arbol['nombre_com']=='Jacarand·']

#print(h)
#len(h)

#4.17 Lista de altos y di√°metros de Jacarand√°

tupla=[(float(arbol['altura_tot']),float(arbol['diametro']))for arbol in arboleda if arbol['nombre_com']=='Jacarand·']
#print(tupla)


#%% 4.18

arboleda= leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarand·']

def medidas_de_especies(especies,arboleda):
    dic={}
    lista_tuplas=[]
    for especie in especies:
        tupla=[(float(arbol['altura_tot']),float(arbol['diametro']))for arbol in arboleda if arbol['nombre_com'] == especie]
        lista_tuplas.append(tupla)#genere lista de tuplas de las 3 especies
    dic={especie:tupla for especie,tupla in zip(especies,lista_tuplas)}
    return dic
#print(dic['Jacarand√°'])
#print(dic)
#print(len(dic['Jacarand√°']))
    #return tupla
#hola =medidas_de_especies(especies,arboleda)
#print(hola)
    
#%% 5.25 Histograma de altos de Jacarand·s
    
nombre_archivo=os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos = [float(arbol['altura_tot'])for arbol in arboleda if arbol['nombre_com']=='Jacarand·']
plt.hist(altos,bins=25)

#%% Scatterplot (di·metro vs alto) de Jacarand·s
def main():
    nombre_archivo=os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    lista_de_pares= tupla=[(float(arbol['altura_tot']),float(arbol['diametro']))for arbol in arboleda if arbol['nombre_com']=='Jacarand·']
    return lista_de_pares

def scatter_hd(lista_de_pares):
    array_pares = np.array(main())#lista_de_pares
    for d,h in array_pares:
        plt.scatter(d,h,alpha=0.4)
        plt.xlabel("diametro (cm)")
        plt.ylabel("alto (m)")
        plt.title("RelaciÛn di·metro-alto para Jacarand·s")
    #print(d,h)
        
#https://stackoverflow.com/questions/66198363/extract-first-column-and-last-column-of-a-numpy-array-and-populate-on-one-dimens