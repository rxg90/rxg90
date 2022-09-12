#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: 
#Borre el else y agregue un upper en el if para que la funcion funcione correctamente en todos los casos
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].upper() == 'A':
            return True
        i +=1
    return False
#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Tal como en el caso anterior, ademas de corregir los errores de sintaxis, 
#agregue upper() para que funcione en todos los casos.

def tiene_a(expresion):#Agregue ":"
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].upper() == 'A': #Agregue ":" y reemplace "=" por "=="
            return True
        i += 1
    return False #remplacé por False

#%%
#Ejercicio 3.3. Función tiene_uno()
def tiene_uno(expresion):
    expresion2=str(expresion)#Agregue la funcion str() y cree una nueva variable,para que convierta la exppresion y funcione en todos los casos
    n = len(expresion2)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion2[i] == '1':
            tiene = True
        i += 1
    return tiene
