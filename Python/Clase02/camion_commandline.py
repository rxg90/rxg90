import csv
import sys
def costo_camion(nombre_archivo):
    path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.'
    f=open(path.format(nombre_archivo),'rt')
    rows=csv.reader(f)
    headers= next(rows)
    precio_total=0
    precio_por_fruta=0
    linea = 0
    for row in rows:
        linea= linea+1
        try:
            precio_por_fruta=float(row[1])*float(row[2])
            precio_total= precio_total+precio_por_fruta
        except ValueError:
            print(f'El archivo tiene datos faltantes en linea {linea}')
    f.close()
    return precio_total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)