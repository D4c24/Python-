#!/usr/bin/python

##############################################
###              By: D4c24                 ###
###    https://github.com/D4c24/Python-    ###
###                                        ###
##############################################
  
########### Ingresar datos en formulario de Logueo

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"c:\driverchrome\chromedriver.exe")
driver.get("https://gmail.com")

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("correo_prueba@gmail.com")
usuario.send_keys(keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("passwordprueba")
clave.send_keys(keys.ENTER)

