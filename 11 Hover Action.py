#!/usr/bin/python

##############################################
###              By: D4c24                 ###
###    https://github.com/D4c24/Python-    ###
###                                        ###
##############################################

##### HOVER ACTION
##### Find_element_by_link_text permite buscar objetos tipo link por el texto plano que dicho objeto tenga.

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path=r"c:\driverchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(3)
elem = driver.find_element_by_link_text

hover = ActionChains(driver).move_to_element(elem)
hover.perform()

##### Displayed elements
from selenium import webdriver
from selenium.webdriver.common.keys improt Keys
import time

driver = driver.Chrome(executable_path=r"c:\driverchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(6)
displayElem = driver.find_element_by_name("btn1")
print(displayElem.is_displayed())  ### Regresa true o False si ya cargo el elemento
print(displayElem.is_enabled())  #### regresa un true o false si el elemento se encuentra disponible
