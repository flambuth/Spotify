# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:13:17 2020

I will write a script that goes through the top20tracks table, get a more detalied look at the artist on each
row, then save that to an artist catalog database.
@author: flamb
"""


import sqlite3
import spotipy
from config import username
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username))

#%% Connect to database, SELECT *

try:
    sqliteConnection = sqlite3.connect('spotify.db')
    cursor = sqliteConnection.cursor()

    sqlite_Query = "select * from daily_top20_tracks;"
    cursor.execute(sqlite_Query)
    print(cursor.fetchall())
    cursor.close()
    
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
        
#%% Create the table that will hold the artist names
        
try:
    sqliteConnection = sqlite3.connect('spotify.db')
    sqlite_create_table_query = '''
                                CREATE TABLE artists (
                                id INTEGER PRIMARY KEY,
                                art_id TEXT NOT NULL,
                                art_name TEXT NOT NULL,
                                followers INTEGER NOT NULL,
                                popularity TEXT NOT NULL);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")


#%%
    
sqliteConnection = sqlite3.connect('spotify.db')
cursor = sqliteConnection.cursor()
    
# for row in cursor.execute('SELECT * FROM daily_top20_tracks;'):
#     print(row)
        
first_song = [i for i in cursor.execute('SELECT * FROM daily_top20_tracks;')][1]
cursor.close()
sqliteConnection.close()

first_artist = sp.artist(first_song[2])

cols = ['genre', 'art_id','art_name','followers', 'popularity', 'album_count', 'first_release']

genre = first_artist['genres'][0]
art_id = first_artist['id']
art_name = first_artist['name']
followers = first_artist['followers']['total']
popularity = first_artist['popularity']
album_count = len(sp.artist_albums(first_artist['id'])['items'])
first_release = min([i['release_date'] for i in sp.artist_albums(first_artist['id'])['items']])

values = [genre, art_id, art_name,followers, popularity, album_count, first_release]
blob = dict(zip(cols, values))

#%%insert into 
sqliteConnection = sqlite3.connect('artists.db')
cursor = sqliteConnection.cursor()


