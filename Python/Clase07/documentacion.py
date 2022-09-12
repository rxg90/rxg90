# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:07:59 2021

@author: rxgfilo
"""

"""
Pensá cuál es el contrato de la función.
Agregale la documentación adecuada.
Comentá el código si te parece que aporta.
Detectá si hay invariantes de ciclo y comentalo al final de la función
"""

def valor_absoluto(n):
    """Dado un numero n, 
    devuelve su valor absoluto"""
    if n >= 0:
        return n
    else:
        return -n
  
def suma_pares(l):
    """Dada una lista, 
    si el elemento es par, lo suma
    y devuelve su resultado"""
    res = 0
    for e in l:
        if e % 2 ==0:#el elemento es par
            res += e
        else:
            res += 0

    return res


def veces(a, b):
    """Dados 2 elementos a y b, 
    suma b veces el elemento a
    y devuelve su resultado"""
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res


def collatz(n):
    """Conjetura de Collatz:
        Dado un número cualquiera, 
        devuelve el numero de iteraciones necesarias 
        hasta llegar a 1"""
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
            #print('if n % 2 == 0',n)
        else:
            n = 3 * n + 1
            #print('else',n)
        res += 1
        #print(res)

    return res
