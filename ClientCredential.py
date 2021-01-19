#! python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:50:41 2020

@author: flamb
"""
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#%%

def get_artist_genre_tags(artist_id):
    '''
    Returns a list that comes from genres key whe using the artist_id endpoint
    '''
    return sp.artist(artist_id)['genres']

def get_artist_top_ten_tracks(artist_id, country='US'):
    '''
    Returns a 2x10 dataframe of the top most played tracks from an artist. Probably
    of all time.
       
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

def get_formatted_artist(art_id):
    sp_object = sp.artist(art_id)
    if len(sp.artist(art_id)['genres']) == 0:
        genre = 'None'
    else:
        genre = sp.artist(art_id)['genres'][0]
    album_count = len(sp.artist_albums(art_id)['items']) 
    first_release = min([i['release_date'] for i in sp.artist_albums(art_id)['items']])
    query_date = query_date = datetime.now().strftime("%Y-%m-%d")
    return [sp_object['id'], sp_object['name'], sp_object['followers'], genre, sp_object['popularity'], album_count, first_release, query_date]
        
#%%
"0DgsuiMZylmPOYkrVOqNYQ"