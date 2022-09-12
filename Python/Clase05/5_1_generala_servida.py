# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:53:44 2021

@author: rxgfilo
"""
import random
import collections

def tirar(n):
    tirada=[]
    for i in range(n):
        tirada.append(random.randint(1,6))
    return tirada


   
def es_generala(tirada):
    generala=all(t==tirada[0] for t in tirada)
    return generala

#%% Simular tiros de generala no servida

def generala_no_servida():
    tiros=0
    m=1
    tirada=tirar(5)#Agregue imput a entrada para poder definir cant de dados que quiero tirar
    ##print(tirada)
    es_generala(tirada)
    while es_generala(tirada)==False and tiros<3:#Mientras no saque generala y los tirossean menos de 3 sigo tirando
        contrep=collections.Counter(tirada)
        repetidos=contrep.most_common(1)
        #print("repetidos",repetidos)
        if repetidos[0][1] ==m:#supongo q si ningun numero se repite quiero tirar todos los dados de nuevo
            generala=[]
        else:
            generala=[repetidos[0][0] for t in range(repetidos[0][1])]
        #print("generala",generala)
        dados_disponibles=len(tirada)-len(generala)
        #print("dados_disponibles",dados_disponibles)
        nueva_tirada=tirar(dados_disponibles)
        #print("nueva_tirada",nueva_tirada)
        for t in nueva_tirada:
            generala.append(t)
        #print("nueva_tirada_final",generala)  
        tirada=generala
        es_generala(tirada)
        #print("tirada_final",tirada)
        tiros +=1
        #print(tiros)
        #print('--------')
    return tirada

#%%                
def prob_generala(N):              
    G = sum([es_generala(generala_no_servida()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')

#Cada 1300 tiradas
