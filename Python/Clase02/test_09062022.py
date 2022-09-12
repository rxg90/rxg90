# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:19:26 2022

@author: rxgfilo
"""

#list of integers that returns the even values that occur on even indexes

list = [2,1,3,4]

#result [4]




def even_list(list):
    new_list=[n for i,n in enumerate(list) if n%2==0 and i%2==0]
    return new_list
    
