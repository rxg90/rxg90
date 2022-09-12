# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:59:38 2021

@author: rxgfilo
"""

# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
#%% 9.6
        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
#%%
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
#%%
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        HTML='<th><th>'.join(headers)
        print(f'<tr><th>{HTML}<th><tr>')

    def fila(self, data_fila):
        HTML='<td><td>'.join(data_fila)
        print(f'<tr><td>{HTML}<td><tr>')
        
#%% 9.7: Polimorfismo en acción
        
def crear_formateador(nombre):
    if nombre == 'txt':
        formateador = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {nombre}')
    return formateador

#%%
    
def imprimir_tabla(camion,lista_columnas,formato):
    formateador=crear_formateador(formato)
    formateador.encabezado(lista_columnas)
    for l in lista_columnas:
        for c in camion:
            formateador.fila(getattr(c,l))
        


        
        
        