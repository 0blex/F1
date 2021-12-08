# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:50:55 2021

@author: alex.black
"""

import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ALEX-DELL;'
                      'Database=F1;'
                      'Trusted_Connection=True')