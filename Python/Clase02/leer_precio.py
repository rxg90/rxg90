import csv
def leer_precio(nombre_archivo):
    diccionario={}
    lista_precios=[]
    path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.'
    with open(path.format(nombre_archivo),'rt') as f:
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

#test=leer_precio('precios.csv')
#print(test)



