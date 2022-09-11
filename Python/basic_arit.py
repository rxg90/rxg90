# -*- coding: utf-8 -*-
'''
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

input: a=3 b=5

output:
8
-2
15

constraints:
1<=a<=10**10
1<=b<=10**10

hacer con funcion y tupla

The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. 
The first line should contain the result of integer division,  // . 
The second line should contain the result of float division,  / .

'''
#a=3 
#b=5
my_tuple=(3,5)
def basic_arit(tuple):
    if 1<=tuple[0]<=10**10 and 1<=tuple[1]<=10**10:
        print(tuple[0] + tuple[1])
        print(tuple[0] - tuple[1])
        print(tuple[0] * tuple[1])
    else: 
        print('Numbers out of range')
        
def py_division(tuple):
    print(tuple[0] // tuple[1])
    print(tuple[0] / tuple[1])
