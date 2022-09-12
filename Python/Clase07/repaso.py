# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:28:34 2021

@author: rxgfilo
"""

from datetime import time

a = time(11, 34, 56)

print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)
#%%

import os
import datetime
import time

camino = '../Clase06/rebotes.py'

stats_archivo = os.stat(camino)

print(time.ctime(stats_archivo.st_atime))
