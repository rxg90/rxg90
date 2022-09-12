def buscar_precio(fruta):
    path=r'C:\Users\RXGFILO\Desktop\ejercicios_python\Data\{}.csv'
    nombre_archivo='precios'
    f=open(path.format(nombre_archivo),'rt')
    precio_cajon=0
    for line in f:
        row=line.split(',')
        if row[0]== fruta:
            precio_cajon = float(row[1])
            print(f'El precio de un cajón de {fruta} es: ${precio_cajon:0.2f}')
            break
    else:
        print(f'{fruta} no figura en el listado de precios')
    f.close()


#test=buscar_precio('Lima')


    
