import csv
def costo_camion(nombre_archivo):
    #path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.csv'
    f=open(nombre_archivo,'rt')
    rows=csv.reader(f)
    headers= next(rows)
    costo_total=0
    precio=0
    #linea = 0
    for n_row,row in enumerate(rows,start=1):
        #linea= linea+1
        record= dict(zip(headers,row))
        try:
            ncajones= int(record['cajones'])
            precio= float(record['precio'])
            costo_total +=ncajones*precio
        except ValueError:
            #print(f'El archivo tiene datos faltantes en fila {linea}')
            print(f'Fila {n_row}: No pude interpretar: {row}')
    f.close()
    return costo_total

#costo = costo_camion('../Data/fecha_camion.csv')
#print('Costo total:', costo)



