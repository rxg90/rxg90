# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:40:38 2021

@author: rxgfilo
"""

def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    lista=sorted(lista)#ordeno la lista
    pos = -1  # comenzamos suponiendo que e no está
    #if lista[-1]<e:#si el ultimo elemento de la lista ordenada es menor que e, no sigo buscando
    #    pos
    #else:
    for i, z in enumerate(lista): # recorremos la lista
        if z>e:
            break
        elif z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos