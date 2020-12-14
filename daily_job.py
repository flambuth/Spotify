# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:03:27 2020

@author: flamb
"""


from Authorization_Code import get_daily_top20_tracks, get_user_top_tracks_artists
import sqlite3



#%% Create the daily 20 tracks dictionary

daily_top_20 = get_daily_top20_tracks()

#%% Establish connection with db

try:
    sqliteConnection = sqlite3.connect('spotify.db')
    cursor = sqliteConnection.cursor()
    sqlite_Query = "select * from daily_top20_tracks;"
    cursor.execute(sqlite_Query)

    
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
    
    
#%% Using the dictionary method

product_sql = '''
INSERT INTO daily_top20_tracks (position, art_id, art_name, album_name, song_id, song_name, popularity, date) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?) '''
    
for i in range(len(daily_top_20['date'])):
    track = [(daily_top_20['position'][i]),
    (daily_top_20['art_id'][i]),
    (daily_top_20['art_name'][i]),
    (daily_top_20['album_name'][i]),
    (daily_top_20['song_id'][i]),
    (daily_top_20['song_name'][i]),
    (daily_top_20['popularity'][i]),
    (daily_top_20['date'][i])]
    cursor.execute(product_sql, track)

    
sqliteConnection.commit()
cursor.close()