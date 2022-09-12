#%% Importar librerias
import csv

from collections import Counter

#%% Definir funciones

def leer_parque (nombre_archivo,parque):
    lista_arboles=[]
    diccionario={}
    #path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.'
    with open(nombre_archivo,'rt',encoding="utf8") as f:
        rows=csv.reader(f)
        headers= next(rows)
        for nrow,row in enumerate(rows):
            record=dict(zip(headers,row))
            if parque in record['espacio_ve']:
                diccionario['long']=float(record['long'])
                diccionario['lat']=float((record['lat']))
                diccionario['id_arbol']=record['id_arbol']
                diccionario['altura_tot']=float(record['altura_tot'])
                diccionario['diametro']=float(record['diametro'])
                diccionario['inclinacio']=float(record['inclinacio'])
                diccionario['id_especie']=float(record['id_especie'])
                diccionario['nombre_com']=record['nombre_com']
                diccionario['nombre_cie']=record['nombre_cie']
                diccionario['tipo_folla']=record['tipo_folla']
                diccionario['espacio_ve']=record['espacio_ve']
                diccionario['ubicacion']=record['ubicacion']
                diccionario['nombre_fam']=record['nombre_fam']
                diccionario['nombre_gen']=record['nombre_gen']
                diccionario['origen']=record['origen']
                diccionario['coord_x']=float(record['coord_x'])
                diccionario['coord_y']=float(record['coord_y'])
                lista_arboles.append(diccionario.copy())
        return lista_arboles
    
def especies(lista_arboles):
    lista_especies=[]
    especie=''
    for l in lista_arboles:
        especie=l['nombre_com']
        lista_especies.append(especie)
    return set(lista_especies)
  

def contar_ejemplares(lista_arboles):
    CantArboles = Counter()
    for l in lista_arboles:
        CantArboles[l['nombre_com']] +=1
    return CantArboles

#%% 3.20 contar ejemplares por especie
        
arbolesGP=leer_parque('../Data/arbolado-en-espacios-verdes.csv','GENERAL PAZ')
arbolesA=leer_parque('../Data/arbolado-en-espacios-verdes.csv','ANDES, LOS')
arbolesC=leer_parque('../Data/arbolado-en-espacios-verdes.csv','CENTENARIO')
especiesGP=especies(arbolesGP)
especiesA=especies(arbolesA)
especiesC=especies(arbolesC)
cantidadGP=contar_ejemplares(arbolesGP)
cantidadA=contar_ejemplares(arbolesA)
cantidadC=contar_ejemplares(arbolesC)
#print(cantidadA)

#Imprimir los 5 arboles mas comunes por parque

print('LOS ANDES')
print('----------')
for especie,count in cantidadA.most_common(5):
    print(especie,count)
    
print('')

print('GENERAL PAZ')
print('----------')
for especie,count in cantidadGP.most_common(5):
    print(especie,count)
    
print('')
    
print('CENTENARIO')
print('----------')
for especie,count in cantidadC.most_common(5):
    print(especie,count)
    


