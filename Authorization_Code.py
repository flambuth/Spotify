# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:56:09 2020

ranges = 
long_term (calculated from several years of data and including all new data as it becomes available), 
medium_term (approximately last 6 months), 
short_term (approximately last 4 weeks)
"""
import pandas as pd
import spotipy
from config import username
from spotipy.oauth2 import SpotifyOAuth
#from collections import Counter


scope = 'user-top-read'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username))

ranges = ['short_term', 'medium_term', 'long_term']

#results = sp.current_user_top_artists()
#results is a dictionary. Keys = ['items', 'total', 'limit', 'offset', 'href', 'previous', 'next']
#results['items'] is a list that holds a dictionary as each item
#   len(results['items']) == 10, the size of the limit parameter
#results['items'] is a dict. Keys = ['external_urls', 'followers', 'genres', 'href', 'id', 'images', 'name', 'popularity', 'type', 'uri']
#%%
def get_user_top_tracks_artists():
    '''
    Returns a 3x20 dataframe of the top most played tracks in user's short term range
    '''
    x = sp.current_user_top_tracks(time_range='short_term')
    cols = ['art_id', 'art_name','album_name','song_id']
    art_id = [i['artists'][0]['id'] for i in x['items']]
    art_name = [i['artists'][0]['name'] for i in x['items']]
    album_name = [i['album']['name'] for i in x['items']]
    song_id = [i['external_urls']['spotify'][-22:-1] for i in x['items']]
    values = [art_id,art_name,album_name,song_id]
    return pd.DataFrame((dict(zip(cols, values))))

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

#%%
#Gets top artist in 3 time ranges
def print_user_top_artists_in_3_ranges():
    ranges = ['short_term', 'medium_term', 'long_term']
    for sp_range in ranges:
        print("range:", sp_range)
        results = sp.current_user_top_artists(time_range=sp_range, limit=10)
        for i, item in enumerate(results['items']):
            print(i, item['name'], item['genres'])
            #print(i, item['name'], '//', item['artists'][0]['name'])
        print()
        
def get_user_top_artists_in_3_ranges():
    '''
    Should return 3 dataframe(short,medium,long). Each dataframe should be 3 cols wide
    and 10 rows.
    '''
    ranges = ['short_term', 'medium_term', 'long_term']
    for sp_range in ranges:
        print("range:", sp_range)
        blob = []
        results = sp.current_user_top_artists(time_range=sp_range, limit=10)
        for i in results['items']:
            blob.append([sp_range,i['name'], i['genres']])
            #print(i, item['name'], '//', item['artists'][0]['name'])
        
    return pd.DataFrame(blob)
    

#%%
#Gets a lot of genres from the long-range parameter

# def get_ulongterm_genres(limit):
#     results = sp.current_user_top_artists(time_range='long_term', limit=limit)
#     for i, item in enumerate(results['items']):
#         print(i, item['name'], item['genres'])
#         #print(i, item['name'], '//', item['artists'][0]['name'])
#     return results

# #makes a list of lists. Each item is a list of genre tags. One list per band
# spam = [i['genres'] for i in results['items']]

# #flattens that list of lists into one big list, with repeats
# flat_list = []
# for sublist in spam:
#     for item in sublist:
#         flat_list.append(item)
        
