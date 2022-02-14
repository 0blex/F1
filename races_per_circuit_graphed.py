# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:10:48 2022

@author: AlexBlack
"""

import pandas as pd
import matplotlib.pyplot as plt

from import_data import races

df = races

races_per_circuit = pd.DataFrame(races.groupby('circuitRef')['raceid'].count()).reset_index()
races_per_circuit.columns = races_per_circuit.columns=['circuitRef','count']
races = races_per_circuit.sort_values('count')
races['circuitRef'] = races['circuitRef'].str.replace('_',' ').str.title()

totalraces = races['count'].sum()
totalcircuits= races['circuitRef'].count()
count = 12
top = races.iloc[-count:totalcircuits]['count'].sum()
rest = races.iloc[:totalcircuits-count]['count'].sum()
check = top+rest==totalraces


fig, ax = plt.subplots(figsize=(12,18))
ax.barh(races['circuitRef'][:totalcircuits-count],
        races['count'][:totalcircuits-count],
        height=0.45, color='#efc74b')
ax.barh(races['circuitRef'][-count:totalcircuits],
        races['count'][-count:totalcircuits],
        height=0.45, color='#881111')
for location in ['left','right','top','bottom']:
    ax.spines[location].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.set_ylim(-2,77.5)
ax.text(x=-10, y=81.5,
        s='Races per Circuit Since 1950',
        weight='bold',size=17)
ax.text(x=-10, y=80,
        s='{} tracks have hosted more races than the other {} combined'.format(count,totalcircuits-12),
        size=12)
ax.set_yticklabels([])
circuits=races['circuitRef']
for i, circuit in zip(range(totalcircuits),circuits):
    ax.text(x=-10,y=i-0.30,
            s=circuit)
ax.axvline(x=35,ymin=0,ymax=76,c='grey',alpha=0.25)
plt.show()




