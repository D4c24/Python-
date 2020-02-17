#!/usr/bin/python

##############################################
###              By: D4c24                 ###
###    https://github.com/D4c24/Python-    ###
###                                        ###
##############################################
    
##### Automatizacion de Select combo box

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class Usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"c:\driverchrome\chromedriver.exe")
        
    def test_selectbox(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        opcion = select.find_elements_by_tag_name("option")
        time.sleep(3)
        for option in opcion:
            print("Los valores son: %s" % option.get_attribute("value"))
            option.click()
            time.sleep(3)
        seleccionar = select(driver.fin_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(3)

if __name__ "" '__main__':
    unittest.main()
