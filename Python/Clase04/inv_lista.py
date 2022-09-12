# Ejercicio 4.5: Invertir una lista

def invertir_lista(lista):
    invertida = []
    i=len(lista)#5
    for e in lista: # Recorro la lista
        i=i-1
        nuevo_elem=lista[i]
        invertida.append(nuevo_elem)#agrego el elemento e al principio de la lista invertida
    return invertida


l = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'] 
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')