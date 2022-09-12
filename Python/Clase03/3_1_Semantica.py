# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:09:34 2021

@author: rxgfilo
"""
"""
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    lista=[]
    while i<n:
        if expresion[i].upper() == 'A':
            resultado = 'true'
            lista.append(resultado)
        i +=1
    if len(lista)>0:
        contiene_a= True
    else:
        contiene_a = False
    return contiene_a

test1=tiene_a('UNSAM 2020')

test2=tiene_a('abracadabra')

test3=tiene_a('La novela 1984 de George Orwell')

"""


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i +=1
    return False
        


test1=tiene_a('UNSAM 2020')
print(test1)
test2=tiene_a('abracadabra')
print(test2)
test3=tiene_a('La novela 1984 de George Orwell')
print(test3)