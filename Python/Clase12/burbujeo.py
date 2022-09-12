# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:47:35 2021

@author: rxgfilo
"""
#lista=[11,3,4,2,1,40,2,8,7,10,25]
"""
def ord_burbujeo(lista):
    compara dos elementos contiguos de la lista y, 
    si el orden es adecuado, los deja como están,
    si no, los intercambia
    n=len(lista)-1
    i=0
    for i in range(0,n):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
            print('primer FOR =',lista)
        for i in range(0,n):
            if lista[i]>lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]
                print('segundo FOR =',lista)
    return lista
"""

def ord_burbujeo(lista):
    """compara dos elementos contiguos de la lista y, 
    si el orden es adecuado, los deja como están,
    si no, los intercambia"""
    n=len(lista)-1 
    i=0
    for i in range(n):
        for i in range(n):  
            if lista[i]>lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]
        n -= 1
    print(lista)
    return lista


#ord_burbujeo([11,3,4,2,1,40,2,8,7,10,25])