# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:24:18 2021

@author: rxgfilo
"""

import fileparse

def leer_camion2(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo) as f:
        camion = fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)
    return camion

def leer_precios2(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe2(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote['nombre']] - lote['precio']
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        lista.append(t)
    return lista