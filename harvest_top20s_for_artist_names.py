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
from datetime import datetime
import pandas as pd

scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username))

#%% 

def retrieve_all_artists_in_db():
    all_the_songs = []

    for track in cursor.execute('SELECT * FROM daily_top20_tracks;'):
        
        if len(sp.artist(track[2])['genres']) == 0:
           genre = 'None'
        else:
            genre = sp.artist(track[2])['genres'][0]
        
        art_id = track[2]
        art_name = track[3]
        followers = sp.artist(track[2])['followers']['total']
        popularity = track[7]
        album_count = len(sp.artist_albums(track[2])['items'])
        first_release = min([i['release_date'] for i in sp.artist_albums(track[2])['items']])
        query_date = datetime.now().strftime("%Y-%m-%d")
    
        values = [art_id, art_name, genre, followers, popularity, album_count, first_release, query_date]
        all_the_songs.append(values)        
        
        all_the_artists = set([i[1] for i in all_the_songs])
    
    return all_the_artists

def find_unique_artists_list(all_the_artists):
    art_names = []
    unique_arts = []
    
    for i in all_the_songs:
        if i[1] not in art_names:
            art_names.append(i[1])
            unique_arts.append(i)
    
    return unique_arts


#%% Create the table that will hold the artist names
  
def create_artists_table():      
    try:
        sqliteConnection = sqlite3.connect('spotify.db')
        sqlite_create_table_query = '''
                                    CREATE TABLE artists (
                                    id INTEGER PRIMARY KEY,
                                    art_id TEXT NOT NULL,
                                    art_name TEXT NOT NULL,
                                    followers INTEGER NOT NULL,
                                    genre STRING NOT NULL,
                                    popularity TEXT NOT NULL,
                                    album_count INTEGER NOT NULL,
                                    first_release TEXT NOT NULL,
                                    query_date TEXT NOT NULL);'''
    
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



#%% Make a list of lists
sqliteConnection = sqlite3.connect('spotify.db')
cursor = sqliteConnection.cursor()

product_sql = '''
INSERT INTO artists (art_id, art_name, genre, followers, popularity, album_count, first_release, query_date) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?) '''


all_the_songs = []

for track in cursor.execute('SELECT * FROM daily_top20_tracks;'):
    
    if len(sp.artist(track[2])['genres']) == 0:
       genre = 'None'
    else:
        genre = sp.artist(track[2])['genres'][0]
    
    art_id = track[2]
    art_name = track[3]
    followers = sp.artist(track[2])['followers']['total']
    popularity = track[7]
    album_count = len(sp.artist_albums(track[2])['items'])
    first_release = min([i['release_date'] for i in sp.artist_albums(track[2])['items']])
    query_date = datetime.now().strftime("%Y-%m-%d")

    values = [art_id, art_name, genre, followers, popularity, album_count, first_release, query_date]
    all_the_songs.append(values)        
    
    all_the_artists = set([i[1] for i in all_the_songs])
    
    art_names = []
    unique_arts = []
    
    for i in all_the_songs:
        if i[1] not in art_names:
            art_names.append(i[1])
            unique_arts.append(i)
    
# sqliteConnection.commit()
# cursor.close()

#%% making changes to ignore artists that are already in the artist table

conn = sqlite3.connect("spotify.db")
df_artists = pd.read_sql_query("select * from artists;", conn)
df_artists = df_artists.set_index('id')
df_songs = pd.read_sql_query('SELECT * FROM daily_top20_tracks;', conn)
df_songs = df_songs.set_index('id')

#artist names that are not in the artist table
artists_to_add = df_songs[~df_songs.art_name.isin(df_artists.art_name)].art_name.unique()

bl

for i in df_songs[df_songs.art_name.isin(artists_to_add)]:
    print(i)
    
def create_unique_artist_rows():
    conn = sqlite3.connect("spotify.db")
    df_artists = pd.read_sql_query("select * from artists;", conn)
    df_artists = df_artists.set_index('id')
    df_songs = pd.read_sql_query('SELECT * FROM daily_top20_tracks;', conn)
    df_songs = df_songs.set_index('id')
    
    #artist names that are not in the artist table
    artists_to_add = df_songs[~df_songs.art_name.isin(df_artists.art_name)].art_name.unique()
    
    df_songs[df_songs.art_name.isin(artists_to_add)]


#%% scratchpad
