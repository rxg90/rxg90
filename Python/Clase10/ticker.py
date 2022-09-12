# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:45:30 2021

@author: rxgfilo
"""

#ticker.py

from vigilante import vigilar
import csv

#%% 10.10: Un pipeline más largo
      
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

"""def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
"""
def parsear_datos(lines):
    headers= ['nombre', 'precio', 'volumen']
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows =(dict(zip(headers, row)) for row in rows)# hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows


#%% 10.11: Filtremos los datos
"""        
def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row


import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
rows = filtrar_datos(rows, camion)
for row in rows:
    print(row)
"""

#%%
from formato_tabla import crear_formateador
import informe_final
   
def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    log = parsear_datos(vigilar(log_file))
    log_filtrado = (l for l in log if l['nombre']in camion)
    #filtrar_datos(log, camion)
    #log_filtrado_dict = dict(log_filtrado)
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre','Precio','Volumen'])
    for l in log_filtrado:
        rowdata = [l['nombre'],f"{l['precio']:0.2f}",f"{l['volumen']:0.2f}"]
        formateador.fila(rowdata)
    """
    informe = informe_final.hacer_informe(camion, rows)
    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    informe_final.imprimir_informe(informe, formateador)
    """
#%%

def f_principal(argumentos):
    informe_camion(argumentos[1], argumentos[2],argumentos[3])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    