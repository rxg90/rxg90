# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:59:12 2021

@author: rxgfilo
"""

import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)


#%% 8.10
dh = df['12-25-2014':].copy()

delta_t = -2 # tiempo que tarda la marea entre ambos puertos
delta_h = 19.5 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()