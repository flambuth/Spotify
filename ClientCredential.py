#! python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:50:41 2020

@author: flamb
"""
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#%%

def get_artist_genre_tags(artist_id):
    return sp.artist(artist_id)['genres']

def get_artist_top_ten_tracks(artist_id, country='US'):
    '''
    Get Spotify catalog information about an artist’s top 10 tracks by country.
    Country set to default. Can only do one country at a time. Set the default for US.
    Not sure what happens if country isn't set.
    https://api.spotify.com/v1/artists/{id}/top-tracks
    '''
    x =  sp.artist_top_tracks(artist_id, country)
    cols = ['song_id', 'song_name'] 
    song_id = [track['uri'][-22:-1] for track in x['tracks']]
    song_name = [sp.track(track['uri'])['name'] for track in x['tracks']]
    values = [song_id,song_name]
    return pd.DataFrame((dict(zip(cols, values))))

def convert_song_id_to_name(song_id):
    return sp.track(song_id)


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
