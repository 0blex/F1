# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 20:57:01 2022

@author: AlexBlack
"""

import pandas as pd
import numpy as np

from config.connect_sql import conn
from functions.functions import read

with open(r'queries\racescircuits.sql', 'r') as file:
    query = file.read()

query = read(r'queries\racescircuits.sql')

df = pd.read_sql(query,conn)
conn.close()

races = df

# number of races 
number_of_seasons = len(races['year'].unique())
first_race_year = races['year'].min()
first_track = races[(races['year']==first_race_year) & (races['round']==1)]['circuitref'][0]

# list of circuits that have held a race
circuitnames = sorted(races['circuitname'].unique())

# list of countries that have held a race
country_most_races = races['country'].describe().loc['top']
italy_races = races[races['country']==country_most_races]
italy_most_common_track = italy_races['circuitref'].describe().loc['top']
monza_races = races[races['circuitref']==italy_most_common_track]
monza_races_count = races[races['circuitref']==italy_most_common_track]['raceid'].count()

years = races['year'].unique().tolist()
monza_years = races[races['circuitref']=='monza']['year'].tolist()


# check which years a track wasnt raced at
def had_ciruit(year,circuit):
    try:
        id = races[(races['year']==year) & (races['circuitref']==circuit)]
        id = id['raceid'].iloc[0].tolist()
        result = isinstance(id, int)
        return result
    except:
        result = False
        return result

def years_no_race(circuit):
    for year in years:
        if had_ciruit(year,circuit)==True:
            pass
        else:
            print(year)
            
years_no_race('monaco')
    
    
# count number of races per year without group function
def count_races(year):
    count = races[races['year']==year]['raceid'].count().tolist()
    return count
    
count_races(1950)

race_count = []
for year in years:
    count = count_races(year)
    race_count.append(count)
    

dict_racecount = {'year'    : years, 
                  'races'   : race_count 
                  }
df_racecount = pd.DataFrame(dict_racecount)


# plot races per year
import matplotlib.pyplot as plt

plt.plot(years,race_count)
plt.xlabel('Year')
plt.ylabel('Number of Races')
plt.title('Races per Year')
plt.show()
