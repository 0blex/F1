# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:19:42 2021

@author: alex.black
"""



import pandas as pd

from functions.functions import csv_upload


circuits = csv_upload('input\\circuits.csv')
constructors = csv_upload('input\\constructors.csv')
constructor_results = csv_upload('input\\constructor_results.csv')
constructor_standings = csv_upload('input\\constructor_standings.csv')
drivers = csv_upload('input\\drivers.csv')
driver_standings = csv_upload('input\\driver_standings.csv')
lap_times = csv_upload('input\\lap_times.csv')
pit_stops = csv_upload('input\\pit_stops.csv')
qualifying = csv_upload('input\\qualifying.csv')
races = csv_upload('input\\races.csv')
results = csv_upload('input\\results.csv')
seasons = csv_upload('input\\seasons.csv')
status = csv_upload('input\\status.csv')


# =============================================================================
# data cleaning to prepare for sql upload
# =============================================================================

races['date'] = pd.to_datetime(races['date']).dt.date
races['time'] = pd.to_datetime(races['time']).dt.time

pit_stops['time'] = pd.to_datetime(pit_stops['time']).dt.time




