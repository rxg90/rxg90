# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 20:09:30 2022

@author: rxg15259
"""
import requests, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

username = "NW-2022-039232"
password = 639430
url= "https://www.cgeonline.com.ar/tramites/citas/modificar/modificar-cita-consulado.html"
exec_path = r"C:\Users\rxg15259\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#driver = webdriver.Chrome(options=options, executable_path=exec_path)# deprecated.
s = Service(exec_path)
driver = webdriver.Chrome(service=s)



driver.get(url)
driver.maximize_window()

time.sleep(15)


# Find the username/email field and send the username to the input field.
uname = driver.find_element("id", "IDU") 
uname.send_keys(username)

time.sleep(5)
pword = driver.find_element("id", "pass") 
pword.send_keys(password)



WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
# Wait for the page to load
driver.implicitly_wait(20)


button = driver.find_element(By.NAME, 'enviar')
button.click()

#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='btnSubmit']"))).click()
#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='btnSubmit']"))).click()
#driver.find_element("name", "enviar").click()
#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME,'enviar'))).click()
'''
driver.find_element(By.CSS_SELECTOR, "#payment > div  > div > iframe") 
and driver.switch_to.frame(iframe)'''
driver.close()