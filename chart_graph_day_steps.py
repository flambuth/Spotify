# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 12:26:44 2021

@author: flamb
"""


import pandas as pd
import sqlite3
from collections import Counter

#%%Read the DataFrame from the SQLITE3 Database

con = sqlite3.connect("spotify.db")
df = pd.read_sql("SELECT * FROM daily_top20_tracks", con).drop('id', axis=1).drop_duplicates()
df.position = df.position.astype('int')

#%% Create Chart_Power calculated field

df['chart_power'] = 21 - df.position

#%%

date_gen = (n for n in df.date.unique())

#%% Find the sum of all the chart_power rows per artist, from first to last day
df.groupby(['art_name'])['chart_power'].sum().sort_values(ascending=False)


#%% each time this line is run, it sums up the chart_power, limited by the date yielded by generator
blob = df[df.date <= next(date_gen)].groupby(['art_name'])['chart_power'].sum().sort_values(ascending=False)
blob.plot.bar()
