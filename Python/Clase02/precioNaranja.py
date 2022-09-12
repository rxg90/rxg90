f=open(r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\precios.csv','rt')

precio_naranja=0

for line in f:
   row=line.split(',')
   if row[0]=='Naranja':
      precio_naranja= float(row[1])
      print(f'El precio de la naranja es ${  precio_naranja:0.2f}')
f.close()
   
