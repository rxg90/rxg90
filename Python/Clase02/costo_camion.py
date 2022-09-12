import csv
def costo_camion(nombre_archivo):
    #path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.csv'
    f=open(nombre_archivo,'rt')
    rows=csv.reader(f)
    headers= next(rows)
    precio_total=0
    precio_por_fruta=0
    #linea = 0
    for n_row,row in enumerate(rows,start=1):
        #linea= linea+1
        try:
            precio_por_fruta=float(row[1])*float(row[2])
            precio_total= precio_total+precio_por_fruta
        except ValueError:
            #print(f'El archivo tiene datos faltantes en fila {linea}')
            print(f'Fila {n_row}: No pude interpretar: {row}')
    f.close()
    return precio_total

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)



