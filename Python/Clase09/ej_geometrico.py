# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:48:05 2021

@author: rxgfilo
"""
import numpy as np
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist_origen(self):
        n = np.sqrt(self.x**2 + self.y**2)
        return n

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'Punto({self.x},{self.y})'

#%% definir clase rectangulo
        
class Rectangulo(Punto):
    def __init__(self,punto1,punto2):

        

        
        