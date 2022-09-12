import csv

#Definir funciones
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


def hacer_informe(lista,diccionario):
   lista_tuplas=[]
   for c in lista:
       if c['nombre'] in diccionario.keys():
               tupla=c['nombre'],c['cajones'],c['precio'],precio[c['nombre']]
               lista_tuplas.append(tupla)
   return lista_tuplas
    
  

#%% Defirnir variables
costo_camion=0
recaudacion=0
camion=leer_camion('../Data/fecha_camion.csv')
precio=leer_precio('../Data/precios.csv')
informe = hacer_informe(camion,precio)


#%% Armar tabla a partir de funcion hacer_informe

def linea_sep():
    print('---------- ---------- ---------- ----------')
    
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s}{headers[3]:>10s}')
linea_sep()
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} ${precio:>10.2f} {cambio:>10.2f}')##Falta agregar $ antes de precio!!!

#%% Obtener el costo del camion y el total vendido
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
