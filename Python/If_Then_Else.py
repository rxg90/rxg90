# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 11:02:51 2022

@author: ASUS-PC
"""
'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20 , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints
1<=n<=100


Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
'''

n = 5

if 1<=n<=100:
    if n%2!=0:
        print('Weird')
    if n%2==0:
        if 2<=n<=5:
            print('Not Weird')
        if 6<=n<=20:
            print('Weird')
        if n>20:
            print('Not Weird')
else:
    print('Integer out of range, n should be betwenn 1 and 100')
    
