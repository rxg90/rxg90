# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:33:19 2021

@author: rxgfilo
"""

#%% 6.6 Parsear un archivo CSV

import csv

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros

#%% 6.7: Selector de Columnas

def parse_csv(nombre_archivo, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

#%% 6.8 Conversion de tipo
    
def parse_csv(nombre_archivo, select = None, types=[str,int,float]):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede transformar el tipo de datos,agregando los tipos a modificar dentro de la lista types.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        # Lee los encabezados del archivo
        encabezados = next(filas)
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        if types:
            filas_conv=[]
            for fila in filas:
              fila = [func(val) for func, val in zip(types, fila)]
              filas_conv.append(fila)
            filas=filas_conv
        else:
            filas
        for fila in filas:
            if not fila:# Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
    
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

#%% 6.9: Trabajando sin encabezados
import csv
    
def parse_csv(nombre_archivo, select = None, types=[str,int,float],has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede transformar el tipo de datos,agregando los tipos a modificar dentro de la lista types.
    Adicionalmente se puede indicar si el archivo tiene headers.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        # Lee los encabezados 
        if has_headers:
            encabezados = next(filas)
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
    
            registros = []
            if types:
                filas_conv=[]
                for fila in filas:
                  fila = [func(val) for func, val in zip(types, fila)]
                  filas_conv.append(fila)
                filas=filas_conv
            else:
                filas
            for fila in filas:
                if not fila:# Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
        
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            registros = []
            if types:
                for fila in filas:
                    if not fila:# Saltear filas vacías
                        continue
                    else:
                      fila = tuple([func(val) for func, val in zip(types, fila)])
                      registros.append(fila)
    return registros
          
                
            
            
            
    