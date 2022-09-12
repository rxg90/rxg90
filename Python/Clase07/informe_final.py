#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

#%% ejercicio 7.7
import fileparse
import lote
import formato_tabla

#%%
def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo) as f:
        camion = fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)
        lote_camion=[lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion]
    return lote_camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote.nombre] - lote.precio
        t = (lote.nombre, lote.cajones, lote.precio, cambio)
        lista.append(t)
    return lista

def imprimir_informe(informe,formateador):
    formateador.encabezado(['Nombre','Cantidad','Precio','Cambio'])
    for nombre,cajones,precio,cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
        

def informe_camion(nombre_archivo_camion, nombre_archivo_precios,fmt='txt'):
    camion = leer_camion(nombre_archivo_camion)
    lista_precios = leer_precios(nombre_archivo_precios)
    precios = dict(lista_precios)
    informe = hacer_informe(camion, precios)
    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)
#%%
def f_principal(argumentos):
    informe_camion(argumentos[1], argumentos[2],argumentos[3])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    






