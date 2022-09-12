# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:56:51 2021

@author: rxgfilo
"""

def medidas_hoja_A(N):
    """Devuelve ancho y largo de la hoja A(N)"""
    if N < 0:
        raise Exception("Por favor ingresar numeros enteros positivos")
    elif N==0:
      (ancho,largo) = (841,1189)
      return (ancho,largo)
    else:
        (ancho,largo) = medidas_hoja_A(N-1)
        
    return(largo//2,ancho)