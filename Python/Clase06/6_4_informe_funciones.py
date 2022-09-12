#%%importar libreria
import csv

#%% 
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
    
#%%
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

#%%
def hacer_informe(lista,diccionario):
   lista_tuplas=[]
   for c in lista:
       if c['nombre'] in diccionario.keys():
               tupla=c['nombre'],c['cajones'],c['precio'],diccionario[c['nombre']]
               lista_tuplas.append(tupla)
   return lista_tuplas


def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)
    

#%% 6.5: Crear una función de alto nivel para la ejecución del programa
def informe_camion(nombre_archivo1,nombre_archivo2):
    camion=leer_camion('../Data/fecha_camion.csv')
    precios=leer_precio('../Data/precios.csv')
    informe = hacer_informe(camion,precios)
    imprimir_informe(informe)


#informe_camion('../Data/camion.csv', '../Data/precios.csv')
