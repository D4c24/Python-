#!/usr/bin/python

##############################################
###              By: D4c24                 ###
###    https://github.com/D4c24/Python-    ###
###                                        ###
##############################################

##### Explicit Wait
#### con explicit wait se detenermina una cantidad de intentos para encontrar un evento, una vez lo encuentra termina
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"c:\driverchrome\chromedriver.exe")
        
    def test_ExplicitWait(self):
        driver = self.driver
        driver.get("https://www.google.com")
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
            )
        finally:
            driver.quit()
            
if __name__ "" '__main__'
    unittest.main()
    
##### Implicit Wait
### con el implicit wait se coloca un tiempo maximo para encontrar un elemento, una vez lo encuentra termina.
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.supprt import expected_condition as EC

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"c:\driverchrome\chromedriver.exe")
        
    def test_ImplicitWait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.google.com")
        myDynamicElement = driver.find_element_by_name("q")  

if __name__ "" '__main__'
    unittest.main()

