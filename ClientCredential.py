#! python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:50:41 2020

@author: flamb
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#%%

def get_artist_genre_tags(artist_id):
    return sp.artist(artist_id)['genres']


#%%
artist_name = []
track_name = []
popularity = []
track_id = []

for i in range(0,10,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
        
#%%
