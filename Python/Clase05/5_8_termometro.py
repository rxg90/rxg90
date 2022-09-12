# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 20:13:56 2021

@author: rxgfilo
"""
import random
import numpy as np

n=999

def medir_temp(n):
    mediciones=[random.normalvariate(37.5,0.2) for i in range(n)]
    np.save('temperaturas',mediciones)
    return mediciones


def resumen_temp(n):
    mx=max(medir_temp(n))
    mn=min(medir_temp(n))
    med=np.percentile(medir_temp(n),50)
    print(f'Hice los calculos {n} veces.EL valor máximo es {mx:.6f}, el mínimo es {mn:.6f}, y la mediana {med:.6f}')