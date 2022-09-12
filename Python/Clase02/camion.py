#costo_camion.py



f=open(r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\camion.csv','rt')

headers= next(f)
precio_total=0
precio_por_fruta=0

for line in f:
    row=line.split(',')
    precio_por_fruta=float(row[1])*float(row[2])
    precio_total= precio_total+precio_por_fruta
print(precio_total)




