# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:10:18 2021

@author: rxgfilo
"""
#%% 9.11
class Canguro():
    def __init__(self,nombre,lista=[]):
        self.nombre=nombre
        self.contenido_marsupio=lista
        
        
    def meter_en_marsupio(self,nuevo_objeto):
        self.contenido_marsupio.append(nuevo_objeto)
        
    def __str__(self):
        return f'El nombre del canguro es: {self.nombre} y su contenido: {self.contenido_marsupio}'   
    def __repr__(self):
        return f'Canguro({self.nombre},{self.contenido_marsupio})'
    

#%% canguro_malo.pyclass Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
        
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
#madre_canguro.meter_en_marsupio('billetera')
#madre_canguro.meter_en_marsupio('llaves del auto')
#madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)