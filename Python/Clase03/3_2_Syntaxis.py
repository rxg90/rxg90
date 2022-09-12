
def tiene_a(expresion):#Agregue ":"
    n = len(expresion)
    print(expresion)
    print(n)
    i = 0
    print(i)
    while i<n:
        if expresion[i] == 'a': #Agregue ":" y reemplace "=" por "=="
            print (expresion[i])
            print(i)
            return True
        i += 1
        print(i)
    return False #remplacé por False


test1=tiene_a('UNSAM 2020')
print('test1:',test1)

#Itera todos los valores, pero como la "A" esta en mayuscula no la toma.
#Ademas 

test3=tiene_a('La novela 1984 de George Orwell')
print('test3:',test3)

