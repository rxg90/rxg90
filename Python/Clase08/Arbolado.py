# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:48:28 2021

@author: rxgfilo
"""



directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)


cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

df_lineal=df[cols_sel]

Arbolado_count=df_lineal['nombre_cientifico'].value_counts(ascending=False)

Arbolado_count.head(10)

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

#%% 8.8: Boxplots

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
