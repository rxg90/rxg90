# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:02:53 2021

@author: rxgfilo
"""

ress, resi,resb,resm = 0,0,0,0
largo_lista=[]
comparaciones_seleccion=[]
for i  in range(3):
    lista=generar_lista(i)#genra lista incremental
    print('lista',lista)
    largo_lista.append(i)
    ress =ord_seleccion(lista.copy())
    print('ress',ress)
    comparaciones_seleccion.append(ress)
    print('comparaciones_seleccion',comparaciones_seleccion)

#print(comparaciones_seleccion,comparaciones_insercion,comparaciones_burbujeo,largo_lista)
grilla_x = np.array(largo_lista)
grilla_y = np.array(comparaciones_seleccion)
plt.plot(grilla_x, grilla_y,c = 'yellow')