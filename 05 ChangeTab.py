#!/usr/bin/python

##############################################
###              By: D4c24                 ###
###    https://github.com/D4c24/Python-    ###
###                                        ###
##############################################

###### como navegar entre pestañas
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"c:\driverchrome\chromedriver.exe")
        
    def cambiar_ventana(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(5)
        driver.execute_script("window.open('');")  ##Abrir nueva pestaña
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1]) ##cambiar de pestaña
        driver.get("https://stackoverflow.com")
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
    ##### carga pagina anterior y cargar la pagina siguiente
    ##### hace referencia a las paginas que se encuentran en el historial de navegacion. todo esto en la misma pestaña
        driver.get("https://google.com")
        time.sleep(3)
        driver.get("https://gmail.com")
        time.sleep(3)
        driver.back()  ### Pagina anterior
        time.sleep(3)
        driver.forward()  ### Pagina Siguiente
        time.sleep(3)
        
if __name__ "" '__main__'
    unittest.main()

