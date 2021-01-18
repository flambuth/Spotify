# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:42:12 2021
Oh these sour times, 'Cause nobody loves me, it's true, Not like you do

@author: flamb
"""

import sqlite3
import spotipy
from datetime import datetime

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username))

sqliteConnection = sqlite3.connect('spotify.db')
cursor = sqliteConnection.cursor()



#%%
known_artists = [i[0] for i in cursor.execute('SELECT DISTINCT art_name FROM daily_top20_tracks;')]
new_songs = []
query = 'SELECT * FROM daily_top20_tracks;'

for track in cursor.execute(query):


    
#this is to check if they already exist in the artist table    
    if track[3] not in known_artists:
         
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
        new_songs.append(values)        
        
        all_the_artists = set([i[1] for i in new_songs])