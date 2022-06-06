# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:32:07 2022

@author: AlexBlack
"""

from config.directories import root
from functions import functions as f


import pandas as pd 
import plotly.express as px 
import streamlit as st 


st.set_page_config(page_title='F1 Races',
                   page_icon=':car:', # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout='wide',
)


# import data from excel and store it in cache

races = f.csv_upload(f'{root}\\input\\cleaned\\races.csv')



# =============================================================================
# SIDEBAR
# =============================================================================
st.sidebar.header('Please Filter Here:')
year = st.sidebar.multiselect(
    'Select Year:',
    options = races['year'].unique(),
    default = races['year'].unique()
)


country = st.sidebar.multiselect(
    'Select Country:',
    options = races['country'].unique(),
    default = races['country'].unique()
)


circuit = st.sidebar.multiselect(
    'Select Track:',
    options = races['circuitRef'].unique(),
    default = races['circuitRef'].unique()
)


df_selection = races.query(
    'year == @year & country == @country & circuitRef == @circuit'
)

# =============================================================================
# Main Page
# =============================================================================

st.title(':car: F1 Race Statistics')
st.markdown('##')

# TOP KPIs
total_races = int(df_selection['raceid'].count())
total_tracks = len(df_selection['circuitID'].unique())
total_countries = len(df_selection['country'].unique())


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
    df_selection.groupby('year')['raceid'].count()
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
    df_selection.groupby('country')['raceid'].count().sort_values(ascending=False)
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
    df_selection.groupby('circuitRef')['raceid'].count().sort_values(ascending=False)
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




# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


































