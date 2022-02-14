# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:20:11 2021

@author: alex.black
"""

import os
import pandas as pd
from functions.functions import csv_upload
from fast_to_sql import fast_to_sql as fts



circuits = csv_upload('input\\circuits.csv')
races = csv_upload('input\\races.csv')
results = csv_upload('input\\results.csv',na='\\N')
constructors = csv_upload('input\\constructors.csv')
drivers = csv_upload('input\\drivers.csv',na='\\N')




from config.connect_sql import conn


try:
    fts.fast_to_sql(circuits, 'circuits', conn, if_exists='replace', custom={'circuitId':'INT PRIMARY KEY',
                                                                             'lat':'DECIMAL(19,8)',
                                                                             'lng':'DECIMAL(19,8)'
                                                                             })
    conn.commit()
    
    
    fts.fast_to_sql(races, 'races', conn, if_exists='replace', custom={'raceId':'INT PRIMARY KEY',
                                                                       'date':'DATE'
                                                                       })    
    conn.commit()
    
    # fts.fast_to_sql(seasons, 'seasons', conn, if_exists='replace', custom={'year':'INT PRIMARY KEY'})    
    # conn.commit()    
    
    # fts.fast_to_sql(qualifying, 'qualifying', conn, if_exists='replace', custom={'qualifyId':'INT PRIMARY KEY'})    
    # conn.commit() 
    
    fts.fast_to_sql(results, 'results', conn, if_exists='replace', custom={'resultId':'INT PRIMARY KEY',
                                                                            'points':'DECIMAL(19,8)'
                                                                            })    
    conn.commit()    
    
    # fts.fast_to_sql(driver_standings, 'driver_standings', conn, if_exists='replace', custom={'driverStandingsId':'INT PRIMARY KEY',
    #                                                                        'points':'DECIMAL(19,8)'
    #                                                                        })    
    # conn.commit() 
    
    # fts.fast_to_sql(constructor_standings, 'constructor_standings', conn, if_exists='replace', custom={'constructorStandingsId':'INT PRIMARY KEY',
    #                                                                                                    'points':'DECIMAL(19,8)'
    #                                                                                                    })    
    # conn.commit() 

    # fts.fast_to_sql(constructor_results, 'constructor_results', conn, if_exists='replace', custom={'constructorResultsId':'INT PRIMARY KEY',
    #                                                                                                'points':'DECIMAL(19,8)'
    #                                                                                                })    
    # conn.commit()     
    
    # fts.fast_to_sql(status, 'status', conn, if_exists='replace', custom={'statusId':'INT PRIMARY KEY'})    
    # conn.commit()     

    fts.fast_to_sql(constructors, 'constructors', conn, if_exists='replace', custom={'constructorId':'INT PRIMARY KEY'})    
    conn.commit()      
    
    fts.fast_to_sql(drivers, 'drivers', conn, if_exists='replace', custom={'driverId':'INT PRIMARY KEY'})    
    conn.commit()  
    
    # fts.fast_to_sql(pit_stops, 'pit_stops', conn, if_exists='replace', custom={'time':'TIME'})    
    # conn.commit()      
    
    # fts.fast_to_sql(lap_times, 'lap_times', conn, if_exists='replace')    
    # conn.commit() 
    
    conn.close()

except:
    conn.close()
    print('upload unsuccessful - sql upload error')