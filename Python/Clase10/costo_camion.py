# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:49:13 2021

@author: rxgfilo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# costo_camion.py

#%% ejercicio 7.5
import informe_final

def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo)
    return camion.precio_total()

def f_principal(argumentos):
    costo = costo_camion(argumentos[1]) 
    print(f'Costo total: {costo}')
#%%    
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    






















