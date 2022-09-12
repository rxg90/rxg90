# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:36:11 2021

@author: rxgfilo
"""

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes
        
    def __iter__(self):
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
    def __len__(self):
        return self.lotes.__len__()
    
    def __getitem__(self,item):
        return self.lotes.__getitem__(item)
    
    def __repr__(self):
        return f'Camion({self.lotes.__repr__()})'
    
    def __str__(self):
        t= ['Camion con '+ str(len(self.lotes)) + ' lotes:']
        for l in self.lotes:
            t.append(l.__str__())
        return '\n'.join(t)
    


            


