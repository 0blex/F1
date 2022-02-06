# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:19:54 2022

@author: alex.black
"""

import pyodbc

from config.connectionstring import connectionstring

conn = pyodbc.connect(connectionstring)
