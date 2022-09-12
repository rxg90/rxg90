# Ejercicio 4.15: Lectura de todos los árboles
import csv 
def leer_arboles(nombre_archivo):
    arboleda=[]
    with open(nombre_archivo,'rt',encoding="utf8") as f:
        rows=csv.reader(f)
        headers= next(rows)
        for nrow,row in enumerate(rows):
            record=dict(zip(headers,row))
            arboleda.append(record)
        return arboleda
            
    

#%% 4.16 Lista de altos de jacaranda

arboleda= leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
#print(arboleda)

h=[float(arbol['altura_tot'])for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

#print(h)
#len(h)

#4.17 Lista de altos y diámetros de Jacarandá

tupla=[(float(arbol['altura_tot']),float(arbol['diametro']))for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
#print(tupla)


#%% 4.18

arboleda= leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies,arboleda):
    dic={}
    lista_tuplas=[]
    for especie in especies:
        tupla=[(float(arbol['altura_tot']),float(arbol['diametro']))for arbol in arboleda if arbol['nombre_com'] == especie]
        lista_tuplas.append(tupla)#genere lista de tuplas de las 3 especies
    dic={especie:tupla for especie,tupla in zip(especies,lista_tuplas)}
    return dic
#print(dic['Jacarandá'])
#print(dic)
#print(len(dic['Jacarandá']))
    #return tupla
#hola =medidas_de_especies(especies,arboleda)
#print(hola)