# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 18:59:31 2022

@author: AlexBlack
"""

import pandas as pd

from config.connect_sql import conn
from functions.functions import read

query = read(r'queries\racescircuits.sql')
races = pd.read_sql(query,conn)

query = read(r'queries\results_enriched.sql')
results = pd.read_sql(query,conn)

results.to_csv('input\\cleaned\\results.csv',index=False)
races.to_csv('input\\cleaned\\races.csv',index=False)

conn.close()
