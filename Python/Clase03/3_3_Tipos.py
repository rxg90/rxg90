

def tiene_uno(expresion):
    expresion2=str(expresion)
    n = len(expresion2)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion2[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)


test1=tiene_uno('UNSAM 2020')
print('test1',test1)
test2=tiene_uno('La novela 1984 de George Orwell')
print('test2',test2)
test3=tiene_uno(1984)
print('test3',test3)