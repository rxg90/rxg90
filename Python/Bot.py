# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:33:50 2022

@author: rxg15259
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

# Open the Website
browser.get('https://www.cgeonline.com.ar/tramites/citas/modificar/modificar-cita-consulado.html')