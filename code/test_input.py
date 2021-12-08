# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:17:45 2021

@author: alex.black
"""

import os
import pandas as pd


root_dir = 'D:\Dropbox (PMX)\Personal Work\Python\Code\Projects\F1\\'
os.chdir(root_dir)


os.chdir(root_dir+'code')
os.getcwd()
from functions import csv_upload


os.chdir(root_dir+'input')


circuits = csv_upload('circuits.csv')
constructors = csv_upload('constructors.csv')
constructor_results = csv_upload('constructor_results.csv')
constructor_standings = csv_upload('constructor_standings.csv')
drivers = csv_upload('drivers.csv')
driver_standings = csv_upload('driver_standings.csv')
lap_times = csv_upload('lap_times.csv')
pit_stops = csv_upload('pit_stops.csv')
qualifying = csv_upload('qualifying.csv')
races = csv_upload('races.csv')
results = csv_upload('results.csv')
seasons = csv_upload('seasons.csv')
status = csv_upload('status.csv')


# =============================================================================
# data cleaning to prepare for sql upload
# =============================================================================

races['date'] = pd.to_datetime(races['date']).dt.date

pit_stops['time'] = pd.to_datetime(pit_stops['time']).dt.time
