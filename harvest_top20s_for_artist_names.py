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

scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username))


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



#%% Goes through the top20tracks table, finds artists not in the artists table 
sqliteConnection = sqlite3.connect('spotify.db')
cursor = sqliteConnection.cursor()
all_the_songs = []

#makes a list of all the artists in the artists table

blob = list(cursor.execute('SELECT DISTINCT art_name FROM artists;'))
blob = [i[0] for i in blob]

for track in cursor.execute('SELECT * FROM daily_top20_tracks;'):


    
#this is to check if they already exist in the artist table    
    if track[3] not in blob:
         
        art_id = track[2]
        art_name = track[3]
        followers = sp.artist(track[2])['followers']['total']
        if len(sp.artist(track[2])['genres']) == 0:
           genre = 'None'
        else:
            genre = sp.artist(track[2])['genres'][0]
#       genre = sp.artist(track[2])['genres'][0]
        popularity = track[7]
        album_count = len(sp.artist_albums(track[2])['items'])
        first_release = min([i['release_date'] for i in sp.artist_albums(track[2])['items']])
        query_date = datetime.now().strftime("%Y-%m-%d")
    
        values = [art_id, art_name, genre, followers, popularity, album_count, first_release, query_date]
        all_the_songs.append(values)        
        
        all_the_artists = set([i[1] for i in all_the_songs])
        
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


#%% Prune the database
product_sql = '''
SELECT DISTINCT art_name,

'''

sqliteConnection = sqlite3.connect('spotify.db')
cursor = sqliteConnection.cursor()
blob = cursor.execute(product_sql)

#%% old functions
        
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

