import random

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        c=0 
        lista_nueva = lista        
    else:
        medio = len(lista) // 2
        izq,c = merge_sort(lista[:medio])
        der,c = merge_sort(lista[medio:])
        lista_nueva,c = merge(izq, der,c)
    return lista_nueva,c

def merge(lista1, lista2,c):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        c += 1   
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado,c

merge_sort([6, 0, 3, 2, 5, 7, 4, 1])
