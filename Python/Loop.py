# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 11:41:38 2022

@author: ASUS-PC
"""
n=3
def ret_sqr(n):
    if 1<=n<=20:
        range_list=[]
        for i in range(n):
            range_list.append(i**2)
            #print(i**2)
        return range_list
        #print(range_list)
    else: 
        print('n is out of range')

my_list= ret_sqr(n)
print(my_list)

