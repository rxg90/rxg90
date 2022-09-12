# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:22:26 2021

@author: rxgfilo
"""

with open('../Data/precios.csv') as f:
    types=[str,float]
    filas = csv.reader(f)
    converted=[]
    # Lee los encabezados del archivo
    encabezados = next(filas)
    for fila in filas:
        fila = tuple([func(val) for func, val in zip(types, fila)])
        converted.append(fila)
    filas=converted
    print(filas)