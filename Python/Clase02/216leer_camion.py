import csv
def leer_camion(nombre_archivo):
    camion=[]
    diccionario={}
    path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.'
    with open(path.format(nombre_archivo),'rt') as f:
        rows=csv.reader(f)
        headers= next(rows)
        for row in rows:
            diccionario['nombre']=row[0]
            diccionario['cajones']=int(row[1])
            diccionario['precio']=float(row[2])
            #print(diccionario)
            camion.append(diccionario.copy())
        return camion
    

test=leer_camion('camion.csv')
#print(test)
lista2=[]
for c in test:
    lista=c['nombre']
    #print(lista)
    lista2.append(lista)
print(lista2)

