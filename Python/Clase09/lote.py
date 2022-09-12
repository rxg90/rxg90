# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:51:33 2021

@author: rxgfilo
"""

class Lote:
    def __init__(self,nombre,cajones,precio):
        self.nombre=nombre
        self.cajones=cajones
        self.precio=precio
        
    def __str__(self):
        return f'({self.nombre},{self.cajones},{self.precio})'
    
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'
    
    def costo(self):
        return (self.cajones*self.precio)
    
    def vender(self,cajones_vendidos):
         self.cajones =(self.cajones-cajones_vendidos)
         
#%% Agregar un metodo nuevo:


class MiLote(Lote):
    def __init__(self, nombre, cajones, precio, factor):
        # Fijate como es el llamado a `super().__init__()`
        super().__init__(nombre, cajones, precio)
        self.factor = factor
    
    def rematar(self):
        self.vender(self.cajones)
    
    def costo(self):
        return self.factor * super().costo()
        
    
         

         