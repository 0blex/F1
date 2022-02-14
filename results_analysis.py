# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:56:43 2022

@author: AlexBlack
"""
import numpy as np
import matplotlib.pyplot as plt

from import_data import results

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

