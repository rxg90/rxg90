# Ejercicio 4.3: Búsquedas de un elemento
from collections import Counter
def buscar_u_elemento(lista,e):
    '''Dada una lista y un elemento, devuelve la posición de la última aparición 
    de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).'''
    pos=-1
    i=0
    for i,z in enumerate(lista):
        if z==e:
            pos=i
    return pos

def buscar_n_elemento(lista,e):
    count=0
    for i,z in enumerate(lista):
        if z==e:
            count += 1
    return count

#test=buscar_n_elemento([1,2,3,2,3,4],1)
#print(test)

#%% Ejercicio 4.4: Búsqueda de máximo y mínimo

def maximo(lista):
    '''Devuelve el máximo de una lista,
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista.
    m=lista[0]# Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e>m:
            m=e
        else:
            m
    return m

