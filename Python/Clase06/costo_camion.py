import informe_funciones

def costo_camion(nombre_archivo):
    rows=informe_funciones.leer_camion(nombre_archivo)
    #headers= next(rows)
    costo_total=0
    precio=0
    for n_row,row in enumerate(rows,start=1):
        try:
            ncajones= row['cajones']
            precio= row['precio']
            costo_total +=ncajones*precio
        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    return costo_total




