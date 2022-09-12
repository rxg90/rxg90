# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:46:35 2021

@author: rxgfilo
"""

def factorial(n):
    if n == 1:
        r = 1
        return r

    f = factorial(n-1)
    r = n * f
    return r

factorial(3)