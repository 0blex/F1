# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 20:57:01 2022

@author: AlexBlack
"""

import pandas as pd
import matplotlib.pyplot as plt

from import_data import races

df = races

circuitnames = sorted(races['circuitname'].unique()) # list of circuits that have held a race

years = races['year'].unique().tolist() # years that held a GP


# plot the number of races per year over time
races_per_year = pd.DataFrame(df.groupby('year')['raceid'].count())

plt.figure(figsize=(16,8))
plt.plot(races_per_year.index,races_per_year['raceid'])
plt.xlabel('Year')
plt.ylabel('Number of Races')
plt.title('Races per Year')
plt.show()

# plot the number of races in each country since first GP
races_per_country = pd.DataFrame(df.groupby('country')['raceid'].count())

plt.figure(figsize=(16,8))
plt.bar(races_per_country.index,races_per_country['raceid'])
plt.xlabel('Country')
plt.xticks(rotation=90)
plt.ylabel('Number of Races')
plt.title('Races per Country')
plt.show()

# plot the number of races at each circuit since first GP
races_per_circuit = pd.DataFrame(df.groupby('circuitref')['raceid'].count())

plt.figure(figsize=(20,8))
plt.bar(races_per_circuit.index,races_per_circuit['raceid'])
plt.xlabel('Circuit')
plt.xticks(rotation=90)
plt.ylabel('Number of Races')
plt.title('Races per Circuit')
plt.show()


