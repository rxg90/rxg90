# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:26:14 2021

@author: rxgfilo
"""

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        p_mitad=lista[:medio]
        s_mitad=lista[medio:]
        if lista[medio]==e:
            res = True
        elif e>lista[medio]:
            bbinaria_rec(s_mitad, e)
        else:
            bbinaria_rec(p_mitad, e)
    

    return res
    
