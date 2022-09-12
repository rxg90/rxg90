# -*- coding: utf-8 -*-
import collections
import random

def cocumpleaños():
    diasaño=[d for d in range(1,366)]
    muestra=random.choices(diasaño,k=30)
    contrep=collections.Counter(muestra)
    repetidos=contrep.most_common()
    return repetidos


def hay_repetidos(lista):
    if lista[0][1]>1:
        return True 
    else:
        return False

def prob_cocumpleaños(N):              
    G = sum([hay_repetidos(cocumpleaños()) for i in range(N)])
    prob = G/N
    print(f'Hice los calculos {N} veces, de las cuales {G} habia mas de una persona que cumplia años el mismo dia.')
    print(f'Podemos estimar la probabilidad de que mas de una persona cumpla años el mismo dia mediante {prob:.6f}.')
    
   