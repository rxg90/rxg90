import csv

##Def funciones
def leer_camion(nombre_archivo):
    camion=[]
    diccionario={}
    #path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.'
    with open(nombre_archivo,'rt') as f:
        rows=csv.reader(f)
        headers= next(rows)
        for nrow,row in enumerate(rows):
            record=dict(zip(headers,row))
            diccionario['nombre']=record['nombre']
            diccionario['cajones']=int(record['cajones'])
            diccionario['precio']=float(record['precio'])
            camion.append(diccionario.copy())
        return camion
    

def leer_precio(nombre_archivo):
    diccionario={}
    #path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.'
    with open(nombre_archivo,'rt') as f:
        rows=csv.reader(f)
        for row in rows:
            if not(row) or row==[]:
                continue
            else:
                #print(row)
                diccionario[row[0]]=float(row[1])
                #lista_precios.append(diccionario.copy())
                #diccionario={}
        return diccionario

#####

costo_camion=0
recaudacion=0
camion=leer_camion('../Data/fecha_camion.csv')
precio=leer_precio('../Data/precios.csv')



#Obtener el costo del camion y el total vendido
for c in camion:
    costo_camion += c['cajones'] * c['precio']
    if c['nombre'] in precio.keys():
      recaudacion +=  c['cajones']*precio[c['nombre']]


#Saber si tuvo ganancia o perdida
diferencia= round(recaudacion-costo_camion,2)

if diferencia >0:
    print(f'La recaudacion fue de ${recaudacion}. \nEl costo del camion fue de ${costo_camion}. \nLa ganancia fue de ${diferencia}')
else:
    diferenciaabsoluta=abs(diferencia)
    print(f'La recaudacion fue de ${recaudacion}. \nEl costo del camion fue de ${costo_camion}. \nLa perdida fue de ${diferenciaabsoluta}')
