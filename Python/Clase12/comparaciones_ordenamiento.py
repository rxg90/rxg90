# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 11:45:56 2021

@author: rxgfilo
"""
import random

def generar_lista(N):
    lista = [0]  * N
    for i in range(N):
      lista[i] = random.randint(1, 1000)
    return lista

#%% ord_seleccion
    
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    c=0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p,c = buscar_max(lista, 0, n,c)
        

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    
    return c

def buscar_max(lista, a, b,c):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
       
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
        c += 1
    return pos_max,c

#ord_insercion(lista)

#%% ord_insercion
    
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    c=0
    for i in range(len(lista) - 1):
        c +=1
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        #print("DEBUG: ", lista,c)
        
    
    return c

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

#ord_insercion([5, 4, 3, 2, 1])  
#%% ord_burbujeo
    
def ord_burbujeo(lista):
    """compara dos elementos contiguos de la lista y, 
    si el orden es adecuado, los deja como están,
    si no, los intercambia"""
    n=len(lista)-1 
    i=0
    c=0
    for i in range(n):
        #print('primer for =',lista,c)
        for i in range(n):  
            c+=1
            if lista[i]>lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]
            #print('segundo for =',lista,c)
        n -= 1
    #print(lista)
    return c

#ord_burbujeo([5, 4, 3, 2, 1])

#%% experimento
from statistics import mean 

def experimento(N,k):
    comp_s=[]
    comp_i=[]
    comp_b=[]
    while k>0:
        lista=generar_lista(N)
        comp_s.append(ord_seleccion(lista.copy()))
        comp_i.append(ord_insercion(lista.copy()))
        comp_b.append(ord_burbujeo(lista.copy()))

        k -=1
    return mean(comp_s),mean(comp_i),mean(comp_b)

#experimento(10, 2)
#%%Comp merge
    
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        c=0 
        lista_nueva = lista        
    else:
        medio = len(lista) // 2
        izq,c = merge_sort(lista[:medio])
        der,c = merge_sort(lista[medio:])
        lista_nueva,c = merge(izq, der,c)
    return lista_nueva,c

def merge(lista1, lista2,c):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        c += 1   
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado,c



#%% experimento_vectores(Nmax)
    
import numpy as np
import matplotlib.pyplot as plt

#Nmax=8
def experimento_vectores(Nmax):
    """Dado un tamaño de lista, devuelve la cantidad 
    de comparaciones que hace cada funcion """
    ress, resi,resb,resm = 0,0,0,0
    largo_lista=[]
    comparaciones_seleccion=[]
    comparaciones_insercion=[]
    comparaciones_burbujeo=[]
    comparaciones_merge=[]
    for i  in range(Nmax):
        lista=generar_lista(i)#genra lista incremental
        largo_lista.append(i)
        ress =ord_seleccion(lista.copy())
        resi =ord_insercion(lista.copy())
        resb =ord_burbujeo(lista.copy())
        resm =merge_sort(lista.copy())
        comparaciones_seleccion.append(ress)
        comparaciones_insercion.append(resi)
        comparaciones_burbujeo.append(resb)
        comparaciones_merge.append(resm[1])
    #print(comparaciones_seleccion,comparaciones_insercion,comparaciones_burbujeo,largo_lista)
    grilla_x = np.array(largo_lista)
    grilla_y = np.array(comparaciones_seleccion)
    grilla_z = np.array(comparaciones_insercion)
    grilla_a = np.array(comparaciones_burbujeo)
    grilla_b=np.array(comparaciones_merge)
    plt.plot(grilla_x, grilla_a,c = 'yellow')
    plt.plot(grilla_x, grilla_y, linestyle='dotted',c = 'blue')
    plt.plot(grilla_x, grilla_z,c = 'red')
    plt.plot(grilla_x, grilla_b, linestyle='dotted',c = 'grey')
    plt.xlabel('Longitud lista')
    plt.ylabel('Cantidad de comparaciones')


#print(len(lista),res/Nmax)
    
