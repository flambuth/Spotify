# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:03:27 2020

@author: flamb
"""


from Authorization_Code import get_daily_top20_tracks, get_user_top_tracks_artists
import sqlite3



#%% Create the daily 20 tracks dictionary

daily_top_20 = get_user_top_tracks_artists()

#%% Establish connection with db

try:
    sqliteConnection = sqlite3.connect('spotify.db')
    cursor = sqliteConnection.cursor()
    sqlite_Query = "select * from daily_top20_tracks;"
    cursor.execute(sqlite_Query)
    print(cursor.fetchall())

    
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
    
    
#%% Insert the daily_top_20 in to the database

generator = daily_top_20.iterrows()

sql_query = '''
INSERT INTO daily_top20_tracks (position, art_id, art_name, album_name, song_id, song_name, popularity, date) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?) '''

for i in list(range(daily_top_20.shape[0])):
    # current_song = next(generator)
    # position = next(lard)[1]['daily_position']
    # art_id = next(lard)[1]['art_id']
    # art_name = next(lard)[1]['art_name']
    # album_name = next(lard)[1]['album_name']
    # song_id = next(lard)[1]['song_id']
    # song_name = next(lard)[1]['song_name']
    # popularity =next(lard)[1]['popularity']
    # date = next(lard)[1]['date']
    
    cursor.execute(sql_query, next(generator)[1].values)


