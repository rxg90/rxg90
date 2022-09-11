# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 12:02:59 2022

@author: ASUS-PC
"""
y=2000

def is_leap(year):
    leap = False
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                leap= True
        else: leap = True
    else: leap
    return leap



print(is_leap(y))       