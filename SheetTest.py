#!/usr/bin/python

##############################################
###              By: D4c24                 ###
###    https://github.com/D4c24/Python-    ###
###                                        ###
##############################################

import gspread
from oauth2client.service_account import ServiceAccountCredentials

## Define the type of privileges that Google API will have Read, write, etc..
scope = ['https://www.googleapis.com/auth/drive'] 

## Here you define the json file who contains all the access credential
creds = ServiceAccountCredentials.from_json_keyfile_name('Automatizacion.json', scope)

## instance the object creds, who have all the credentials
client = gspread.authorize(creds)

## Call a data form an especific cell, column, etc..
sheet = client.open('Creds_Test').sheet1
"""
data = sheet.get_all_records()
data = sheet.row_values(3)
data = sheet.col_values(1)
sheet.update_cell(2,1, "hello")

row = ["lenin", "carl"]
index = 2

sheet.insert_row(row, index)
"""

data = sheet.cell(2, 2).value

## Print results
print(data)
