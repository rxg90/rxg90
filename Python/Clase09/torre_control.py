# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 08:47:07 2021

@author: rxgfilo
"""

class TorreDeControl:
    
    def __init__(self):
        """Crea cola vacia"""
        self.cola_arribo = []
        self.cola_partida=[]
        
    def nuevo_arribo(self,avion):
       self.cola_arribo.append(avion)
       
    def nueva_partida(self,avion):
        self.cola_partida.append(avion)
    
    
    def ver_estado(self):
        if len(self.cola_arribo)== 0 and len(self.cola_partida)==0:
         print('No hay vuelos pendientes')
        else:
            estado='Vuelos esperando para aterrizar: '
            estado +=','.join(self.cola_arribo)
            estado += '\n'
            estado += 'Vuelos esperando para despegar: '
            estado += ','.join(self.cola_partida)
            print(estado)
            
    def asignar_pista(self):
        if len(self.cola_arribo)>0:
            #print('hola')
            print(f'El vuelo {self.cola_arribo[0]} aterrizo con exito')
            self.cola_arribo.pop(0)
            #return self.cola_arribo
        elif len(self.cola_partida)>0:
            print(f'el vuelo {self.cola_partida[0]} aterrizo con exito')
            self.cola_partida.pop(0)
        else:
           print('No hay vuelos en espera')
        #return pista
        
        
            
        