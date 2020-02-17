#!/usr/bin/python

##############################################
###              By: D4c24                 ###
###    https://github.com/D4c24/Python-    ###
###                                        ###
##############################################

#### click en un toogle o switch

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"c:\driverchrome\chromedriver.exe")
    
    def test_usando_toggle(self)
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(3)
        toggle = driver.find_element_by _xpath("//*[@id='main']/label[3]/div")
        toogle.click()
        time.sleep(3)
        toogle.click()
        time.sleep(3)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ "" '__main__':
    unittest.main()
