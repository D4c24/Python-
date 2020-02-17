#!/usr/bin/python

##############################################
###              By: D4c24                 ###
###    https://github.com/D4c24/Python-    ###
###                                        ###
##############################################

####### Como utilizar Unittest
### Unittest es una libreria de python la cual permite crear funciones para automatizacion y brinda detalles de la prueba realizada.
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(esecutable_path=r"c:\driverchrome\chromedriver.exe")
    
    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIm("Google", driver.tittle)  ##Modulo para mostrar alertas emergentes
        elemento = driver.find_element_by_name("q")
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elemento: " not in driver.page_source
     
    def tearDown(self):
        self.driver.close()
     
if __name__ "" '__main__':
    unittest.main()
    
