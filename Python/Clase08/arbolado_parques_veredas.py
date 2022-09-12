# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:24:47 2021

@author: rxgfilo
"""

#%% Librerias

import pandas as pd
import seaborn as sns
import os

#%% 8.9: Comparando especies en parques y en veredas


directorio = '../Data'
parques = 'arbolado-en-espacios-verdes.csv'
veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_parques = os.path.join(directorio,parques)
fname_veredas = os.path.join(directorio,veredas)

cols_sel_parques = ['nombre_cie', 'diametro', 'altura_tot']
cols_sel_veredas = ['nombre_cientifico','diametro_altura_pecho', 'altura_arbol']

#Crear DF
df_parques = pd.read_csv(fname_parques)
df_veredas = pd.read_csv(fname_veredas)


#Filtrar solo por Tipas
df_tipas_parques= df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_sel_parques].copy()


df_tipas_veredas= df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols_sel_veredas].copy()

#Renombrar columnas
df_tipas_veredas=df_tipas_veredas.rename(columns={'nombre_cientifico':'nombre_cie','diametro_altura_pecho':'diametro','altura_arbol':'altura_tot'})

#Agregar columna nueva ambiente

df_tipas_parques['ambiente'] = 'parque'
 
df_tipas_veredas['ambiente'] = 'vereda'

#Joinear ambos DF

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#Crear boxplot para diametro

df_tipas.boxplot('diametro',by = 'ambiente')

# Crear boxplot para altura
df_tipas.boxplot('altura_tot',by = 'ambiente')

#%% Definir funcion
def boxplot_por_especie(especie_parques,especie_veredas,tipo):
    directorio = '../Data'
    parques = 'arbolado-en-espacios-verdes.csv'
    veredas = 'arbolado-publico-lineal-2017-2018.csv'
    fname_parques = os.path.join(directorio,parques)
    fname_veredas = os.path.join(directorio,veredas)
    
    cols_sel_parques = ['nombre_cie', 'diametro', 'altura_tot']
    cols_sel_veredas = ['nombre_cientifico','diametro_altura_pecho', 'altura_arbol']
    
    #Crear DF
    df_parques = pd.read_csv(fname_parques)
    df_veredas = pd.read_csv(fname_veredas)
    df_tipas_parques= df_parques[df_parques['nombre_cie'] == especie_parques][cols_sel_parques].copy()


    df_tipas_veredas= df_veredas[df_veredas['nombre_cientifico'] == especie_veredas ][cols_sel_veredas].copy()
    
    #Renombrar columnas
    df_tipas_veredas=df_tipas_veredas.rename(columns={'nombre_cientifico':'nombre_cie','diametro_altura_pecho':'diametro','altura_arbol':'altura_tot'})
    
    #Agregar columna nueva ambiente
    
    df_tipas_parques['ambiente'] = 'parque'
     
    df_tipas_veredas['ambiente'] = 'vereda'
    
    #Joinear ambos DF
    
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    
    #Crear boxplot para diametro
    
    df_tipas.boxplot(tipo,by = 'ambiente')

