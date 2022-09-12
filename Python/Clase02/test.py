# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:06:09 2021

@author: rxgfilo
"""

import csv
def leer_camion(nombre_archivo):
    'Computa el precio total del camion (cajones * precio) de un archivo'
    camion=[]
    diccionario={}
    path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.'
    with open(path.format(nombre_archivo),'rt') as f:
        rows=csv.reader(f)
        headers= next(rows)
        for row in rows:
            diccionario['nombre']=row[0]
            diccionario['cajones']=int(row[1])
            diccionario['precio']=float(row[2])
            camion.append(diccionario)
        print(camion)
    #return output_dict


camion=leer_camion('camion.csv')
print(camion)