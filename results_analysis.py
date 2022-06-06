# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:56:43 2022

@author: AlexBlack
"""
import numpy as np
import matplotlib.pyplot as plt

from import_data import results
from functions.functions import log

# explore data
df = results

df['altitude'].describe()
df['altitude'].value_counts()

alts = df['altitude'].value_counts().reset_index() # check alt data for none int data
noAlt = df[df['altitude']=='\\N']
# circuitID = 78 - Quatar - losail

losail = df[df['circuitRef']=='losail'] 

# no altitude data for these tracks in data set so google search to find
# losail is 16m 
df.loc[df['circuitID']==78,'altitude']='16'
df['altitude'] = df['altitude'].astype(np.int64)


# =============================================================================
# cummulative results per driver plot
# =============================================================================
results2021 = df[df['year']==2021]
drivers2021 = list(results2021['driverID'].unique())
rounds2021 = list(range(1,23))


results2021['cummPoints'] = 0
cumm_driver = results2021[['resultID','raceID','driverID']]
cumm_driver['cummPoints'] = 0

# driver = 830
# round = 2
# resultID = 24986
for driver in drivers2021:
    df = results2021[results2021['driverID']==driver][['resultID','round','points']]
    rounds = list(df['round'])
    for round in rounds:
        resultindex  = df[df['round']==round].index[0]
        points = df[df['round']<=round]['points'].sum()
        results2021.loc[resultindex,'cummPoints'] = points
        cumm_driver.loc[resultindex,'cummPoints'] = points
        log('{} - {} loaded'.format(driver,round))

'''
filter to each driver 
sort rows by round number
for round 1 cummPoints equals points
then from round two sum points above



'''
