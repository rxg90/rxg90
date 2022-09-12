# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:04:50 2021

@author: rxgfilo
"""
#%% import libraries
from datetime import timedelta,datetime,date
import numpy as np


#%% 8.1
def vida_en_segundos(fecha_nac):
    fecha_nac_dt=datetime.strptime(fecha_nac,'%d/%m/%Y')
    fecha_hoy= datetime.now()
    #return fecha_hoy
    delta_fecha=fecha_hoy-fecha_nac_dt
    delta_fecha_seg=delta_fecha.total_seconds()
    return delta_fecha_seg


#%% 8.2 Dias para la primavera
    
def dias_para_primavera(fecha_primavera):
    fecha_hoy = datetime.now()
    primavera= datetime.strptime(fecha_primavera,'%d/%m/%Y')
    dias_para_primavera=primavera-fecha_hoy
    return dias_para_primavera.days

#%% 8.3 Fecha de reincorporación
    
def fecha_reincorporacion(inicio_licencia,cant_dias):
    inicio= datetime.strptime(inicio_licencia,'%d/%m/%Y')
    reincorporacion = inicio+timedelta(days=200)
    return reincorporacion


#%% 8.4: Días hábiles
    
def dias_habiles(inicio,fin,feriados):
    cant_feriados=len(feriados)
    inicio_dt= datetime.strptime(inicio,'%d/%m/%Y').strftime('%Y-%m-%d')
    fin_dt= datetime.strptime(fin,'%d/%m/%Y').strftime('%Y-%m-%d')
    laborales=(np.busday_count(inicio_dt,fin_dt))-cant_feriados
    return laborales

#%% Cambiar atributos de un archivo
    
import os
import datetime
import time

camino = '../Clase06/rebotes.py'

stats_archivo=os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso=datetime.datetime(year=2017,month=9,day=21,hour=19,minute=51,second=0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso=fecha_acceso.timestamp()
ts_modifi=fecha_modifi.timestamp()
os.utime(camino,(ts_acceso, ts_modifi))

stats_archivo=os.stat(camino)


print(time.ctime(stats_archivo.st_atime))




    

    