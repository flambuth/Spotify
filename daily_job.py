# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:03:27 2020
It's been 97 days since I've laid my head beside you
And a million miles of highway in between
@author: flamb
"""


from Authorization_Code import get_daily_top20_tracks, get_top_artists
from harvest import find_new_artists_in_tracks, upload_new_artists
import sqlite3
#from datetime import datetime


#%% Create the daily 20 tracks dictionary

daily_top_20 = get_daily_top20_tracks()
daily_top_artists = get_top_artists()

# product_sql = '''
# INSERT INTO daily_top20_tracks (position, art_id, art_name, album_name, song_id, song_name, popularity, date) 
# VALUES (?, ?, ?, ?, ?, ?, ?, ?) '''

#%% Write to the Database the day's top 20 tracks

# try:
#     sqliteConnection = sqlite3.connect('spotify.db')
#     cursor = sqliteConnection.cursor()
#     sqlite_Query = "select * from daily_top20_tracks;"
#     cursor.execute(sqlite_Query)
#     for i in range(len(daily_top_20['date'])):
#         track = [(daily_top_20['position'][i]),
#         (daily_top_20['art_id'][i]),
#         (daily_top_20['art_name'][i]),
#         (daily_top_20['album_name'][i]),
#         (daily_top_20['song_id'][i]),
#         (daily_top_20['song_name'][i]),
#         (daily_top_20['popularity'][i]),
#         (daily_top_20['date'][i])]
#         cursor.execute(product_sql, track)
    
# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)

# sqliteConnection.commit()
# cursor.close()
    
#%%    

product_sql = '''
INSERT INTO daily_top20_tracks (position, art_id, art_name, album_name, song_id, song_name, popularity, date) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?) '''

sqliteConnection = sqlite3.connect('spotify.db')
cursor = sqliteConnection.cursor()
    
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
sqliteConnection.close()

#%% Refactoring to make a function. Then repeat that function call for the daily top 20 
artists_sql = '''
INSERT INTO daily_top20_artists(position, art_id, art_name, popularity, followers, date) 
VALUES (?, ?, ?, ?, ?, ?) '''

sqliteConnection = sqlite3.connect('spotify.db')
cursor = sqliteConnection.cursor()
    
for i in range(len(daily_top_artists['date'])):
    artist = [(daily_top_artists['position'][i]),
    (daily_top_artists['art_id'][i]),
    (daily_top_artists['art_name'][i]),
    (daily_top_artists['popularity'][i]),
    (daily_top_artists['followers'][i]),   
    (daily_top_artists['date'][i])]
    cursor.execute(artists_sql, artist)
    
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()

#%% Harvests the top20_tracks database for new artists. They are added to the artist table if there is at least one.
blob = find_new_artists_in_tracks()
if len(blob) > 0:
    upload_new_artists(blob)