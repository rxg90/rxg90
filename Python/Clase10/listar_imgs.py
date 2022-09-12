# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 20:42:13 2021

@author: rxgfilo
"""

#%% 8.5 Recorrer el arbol de archivos
import os
               
#directorio= '../Data/ordenar'
def archivos_png(directorio):
    files_list=[]
    for root, dirs, files in os.walk(directorio):
        for name in files:
            filename, extention = os.path.splitext(name)
            #print(extention)
            if extention =='.png':
                files_list.append(name)
    #print(name)
    return files_list


if __name__ == '__main__':
    import sys
    print(archivos_png(sys.argv[1]))
    
#%% 8.6: Ordenar el árbol de archivos (optativo)
    
