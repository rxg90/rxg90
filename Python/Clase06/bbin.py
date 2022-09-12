# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:39:15 2021

@author: rxgfilo
"""

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

#%%
def donde_insertar(lista,x):
    pos=0
    for i, z in enumerate(lista): # recorremos la lista
        if z==x:#si encuentra e
            pos=i#guada posicion
            break#sale del ciclo
        elif x>lista[i] and x<lista[i+1]:
            pos = i+1 
            break 
        elif x >lista[-1]:
            pos=len(lista)
            break
        elif x< lista[0]:
            pos=0
            break
    return pos


#%% 6.15: Insertar un elemento en una lista
    
def insertar(lista,x):
    pos=0
    for i, z in enumerate(lista): # recorremos la lista
        if z==x:#si encuentra e
            pos=i#guada posicion
            break#sale del ciclo
        elif x>lista[i] and x<lista[i+1]:
            pos = i+1 
            lista.insert(pos,x)
            break  
        elif x >lista[-1]:
            pos=len(lista)
            lista.insert(pos,x)
            break
        elif x< lista[0]:
            pos=0
            lista.insert(pos,x)
            break
    return pos,lista

 #%%

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

#%% ver cantidad de comparaciones
    
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    comps = 0
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        comps +=1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos,comps