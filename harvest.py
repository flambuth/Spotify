# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:42:12 2021
Oh these sour times, 'Cause nobody loves me, it's true, Not like you do

@author: flamb
"""

import sqlite3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

from config import username

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username))

sqliteConnection = sqlite3.connect('spotify.db')
cursor = sqliteConnection.cursor()

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

#%%Find artists in Top20 table that are not in the Artist table
def find_new_artists_in_tracks():
    connection = sqlite3.connect('spotify.db')
    cursor = connection.cursor()
    
    known_artists = [i[0] for i in cursor.execute('SELECT DISTINCT art_name FROM artists;')]
    new_songs = []
    query = 'SELECT * FROM daily_top20_tracks;'
    
    for track in cursor.execute(query):
    
    
        
    #this creates a list of lists. Each item on the list is a row for the artist table
        if track[3] not in known_artists:
             
            art_id = track[2]
            art_name = track[3]
            followers = sp.artist(track[2])['followers']['total']
            if len(sp.artist(track[2])['genres']) == 0:
               genre = 'None'
            else:
                genre = sp.artist(track[2])['genres'][0]
            popularity = track[7]
            album_count = len(sp.artist_albums(track[2])['items'])
            first_release = min([i['release_date'] for i in sp.artist_albums(track[2])['items']])
            query_date = datetime.now().strftime("%Y-%m-%d")
        
            values = [art_id, art_name, followers, genre, popularity, album_count, first_release, query_date]
            new_songs.append(values)
            known_artists.append(art_name)
    connection.commit()
    cursor.close()
    connection.close()
    return new_songs
        
#%%Add artists to artist table
        
def upload_new_artists(new_songs):
    product_sql = '''
    INSERT INTO artists (art_id, art_name, followers, genre, popularity, album_count, first_release, query_date) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?) '''
    
    
    sqliteConnection = sqlite3.connect('spotify.db')
    cursor = sqliteConnection.cursor()
        
    for song in new_songs:
        cursor.execute(product_sql, song)
        
    sqliteConnection.commit()
    cursor.close()
    sqliteConnection.close()

