# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:01:59 2021

@author: rxgfilo
"""

#larenga.py

def pascal(n,k):
    if k==n:
        return 1
    elif k==0:
        return 1
    else:
     return pascal(n-1,k-1)+pascal(n-1,k)