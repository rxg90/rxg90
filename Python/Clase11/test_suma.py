# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:48:27 2021

@author: rxgfilo
"""

# 11.3 digitos:

def cant_digitos(n):
    if n//10 ==0:
        return 1
    else:
       return cant_digitos(n//10) + 1
   
#%% 11.4 potencias
       
def es_potencia(n,b):
    if n // b ==0:
        return True
    else:
        return es_potencia(n,b)
        