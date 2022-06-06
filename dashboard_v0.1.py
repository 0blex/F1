# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:32:07 2022

@author: AlexBlack
"""

from config.directories import root
from functions import functions as f


import pandas as pd 
import numpy as np
import plotly.express as px 
import streamlit as st 


st.set_page_config(page_title='F1 Races',
                   page_icon=':car:', # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout='wide',
)


# import data from excel and store it in cache

races = f.csv_upload(f'{root}\\input\\cleaned\\races.csv')
results = f.csv_upload(f'{root}\\input\\cleaned\\results.csv')


# =============================================================================
# Main Page
# =============================================================================

st.title(':car: F1 Race Statistics')
st.markdown('##')

# TOP KPIs
total_races = int(races['raceid'].count())
total_tracks = len(races['circuitID'].unique())
total_countries = len(races['country'].unique())
total_years = len(races['year'].unique())


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Total Races:')
    st.subheader(f':checkered_flag: {total_races:,}')
    
with middle_column:
    st.subheader('Total Countries:')
    st.subheader(f':earth_africa: {total_countries}')
    
with right_column:
    st.subheader('Total Tracks:')
    st.subheader(f':round_pushpin: {total_tracks}')




# RACES PER YEAR [BAR CHART]
races_per_year = (
    races.groupby('year')['raceid'].count()
)

fig_races_year = px.line(
    races_per_year,
    x=races_per_year.index,
    y='raceid',
    title='<b>Races Per Year</b>',
    template='plotly_white',
    labels=dict(year='Year',raceid='Races')
    )
fig_races_year.update_layout(
    plot_bgcolor = 'rgba(0,0,0,0)',
    xaxis = (dict(showgrid=False)) 
)


with left_column:
    st.plotly_chart(fig_races_year)


# RACES PER COUNTRY
# it will be cool to get the cooridinates from geo scatter and plot a map of all places where a races took place - next iteration
races_per_country = (
    races.groupby('country')['raceid'].count().sort_values(ascending=False)
)

fig_races_country = px.bar(
    races_per_country,
    x=races_per_country.index,
    y='raceid',
    title='<b>Races Per Country</b>',
    template='plotly_white',
    labels=dict(country='Country',raceid='Races')
)
fig_races_year.update_layout(
    plot_bgcolor = 'rgba(0,0,0,0)',
    xaxis = (dict(showgrid=False))
)


with middle_column:
    st.plotly_chart(fig_races_country)


# RACES PER TRACK
races_per_track = (
    races.groupby('circuitRef')['raceid'].count().sort_values(ascending=False)
)

fig_races_track = px.bar(
    races_per_track,
    x=races_per_track.index,
    y='raceid',
    title='<b>Races Per Track</b>',
    template='plotly_white',
    labels=dict(circuitRef='Track',raceid='Races')
)
fig_races_year.update_layout(
    plot_bgcolor = 'rgba(0,0,0,0)',
    xaxis = (dict(showgrid=False))
)


with right_column:
    st.plotly_chart(fig_races_track)


st.markdown('---')







# =============================================================================
# SIDEBAR
# =============================================================================
# st.sidebar.header('Please Filter Here:')
# year = st.sidebar.selectbox(
#     'Select Year:',
#     options = races['year'].sort_values(ascending=False).unique(),
#     index = 1
#     #default = races['year'].unique() # commented out due to use of single select dropdown 'selectbox
# )


year = st.selectbox(
    'Select Year:',
    options = races['year'].sort_values(ascending=False).unique(),
    index = 1
    #default = races['year'].unique() # commented out due to use of single select dropdown 'selectbox
)

df_selection = results.query(
    'year == @year'
)



# =============================================================================
# LOWER PAGE 
# =============================================================================
st.header(f'{year} Constructor Battle')


# CONSTRUCTOR WINNER KPIs
constructor_season_winner = results[results['year']==year].groupby('constructorName').sum()['points'].sort_values(ascending=False).index[0]
constructor_season_winner_points = results[results['year']==year].groupby('constructorName').sum()['points'].sort_values(ascending=False).iloc[0]
constructor_season_winner_races_won = results[(results['year']==year) & (results['constructorName']==constructor_season_winner) & (results['racePosition']==1)]['raceID'].count()

constructor_season_winner_podiums = results[(results['year']==year) & (results['constructorName']==constructor_season_winner) & (results['racePosition']<=3)]['raceID'].count()
constructor_season_winner_dnfs = results[(results['year']==year) & (results['constructorName']==constructor_season_winner) & (results['racePosition'].isnull())]['raceID'].count()

constructor_season_top_3 = results[results['year']==year].groupby('constructorName').sum()['points'].sort_values(ascending=False).index[0:3].to_list()

# TOP 3 CONSTRUCTORS LINE GRAPH DATA SET
def get_cumm_constructor():
    '''calculate the cummulative points for each constructor'''
    results = df_selection[df_selection['year']==year]
    constructors = list(results['constructorName'].unique())
    rounds = list(results['round'].unique())
    
    cumm_constructor = results.groupby(['round','constructorName']).sum()['points'].reset_index()
    cumm_constructor['cummPoints'] = 0
    
    for constructor in constructors:
        df = cumm_constructor[cumm_constructor['constructorName']==constructor]
        
        for round in rounds:
            resultindex  = df[df['round']==round].index[0]
            points = df[df['round']<=round]['points'].sum()
            cumm_constructor.loc[resultindex,'cummPoints'] = points
    
    cumm_constructor = cumm_constructor.drop(columns=('points'))
    
    return cumm_constructor


cumm_constructor = get_cumm_constructor()

Cumm_constructor_top_3 = cumm_constructor[cumm_constructor['constructorName'].isin(constructor_season_top_3)]


# TOP 3 CONSTRUCTORS LINE GRAPH PLOTTING
fig_top_3 = px.line(
    Cumm_constructor_top_3,
    x='round',
    y='cummPoints',
    title='<b>Top 3 Constructor Points</b>',
    width=600, height=600,
    color = 'constructorName',
    template='plotly_white',
    labels=dict(round='Round',cummPoints='Points')
)
fig_top_3.update_layout(
    plot_bgcolor = 'rgba(0,0,0,0)',
    xaxis = (dict(showgrid=False)),
    legend=dict(
        title=None, orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"
    )
)




left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('##')
    st.subheader(f'Total Points: {constructor_season_winner_points}') #can add a country flag from a dictionary lookup here


with middle_column:
    st.subheader('Season Winner:')
    st.subheader(f':trophy: {constructor_season_winner} :trophy:')


with right_column:
    st.subheader('##')
    st.subheader(f'Races Won: {constructor_season_winner_races_won}') 

st.markdown('##')



with st.container():
    graph_column, stats_column = st.columns((2,1))
    
    with graph_column:
        st.plotly_chart(fig_top_3,use_container_width=True)


    with stats_column:
        ## insert season race stats
        st.subheader(f'Races Won: {constructor_season_winner_races_won}') # insert horizontal bar chart alongside
        
        st.subheader(f'Podiums: {constructor_season_winner_podiums}')
        
        st.subheader(f'DNFs: {constructor_season_winner_dnfs}')
        
# CONSTRUCTOR SEASON POINTS GRAPH

























driver_season_winner = results[results['year']==year].groupby('driverName').sum()['points'].sort_values(ascending=False).index[0]





#st.dataframe(df_selection)












'''Page End'''



















# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


































