#!/usr/bin/python

##############################################
###              By: D4c24                 ###
###    https://github.com/D4c24/Python-    ###
###                                        ###
##############################################

######### Codigo muestra ####################
## Chrome:https://sites.google.com/a/chromium.org/chromedriver/downloads
## Firefox:https://github.com/mozilla/geckodriver/releases
##Abrir navegador en una pagina especifica, Para ello se utiliza el driver especifico del navegador.

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"c:\driverchrome\chromedriver.exe")
driver.get("https://python.org")
driver.close()
