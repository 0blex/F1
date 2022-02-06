# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:50:55 2021

@author: alex.black
"""

driver = 'SQL Server'
server = 'localhost\SQLEXPRESS'
database = 'F1'

connectionstring = 'Driver={};Server={};Database={};Trusted_Connection=True'.format(driver,server,database)


