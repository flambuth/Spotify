# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:56:09 2020

ranges = 
long_term (calculated from several years of data and including all new data as it becomes available), 
medium_term (approximately last 6 months), 
short_term (approximately last 4 weeks)
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import Counterfrom collections import Counter

scope = 'user-top-read'
username = 'lambuth'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=username))

ranges = ['short_term', 'medium_term', 'long_term']

#results = sp.current_user_top_artists()
#results is a dictionary. Keys = ['items', 'total', 'limit', 'offset', 'href', 'previous', 'next']
#results['items'] is a list that holds a dictionary as each item
#   len(results['items']) == 10, the size of the limit parameter
#results['items'] is a dict. Keys = ['external_urls', 'followers', 'genres', 'href', 'id', 'images', 'name', 'popularity', 'type', 'uri']


#%%
#Gets top artist in 3 time ranges
for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_artists(time_range=sp_range, limit=10)
    for i, item in enumerate(results['items']):
        print(i, item['name'])
        #print(i, item['name'], '//', item['artists'][0]['name'])
    print()
    
#%%
#Gets top artist in 3 time ranges, and the genre tags that are saved with the artist name.

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_artists(time_range=sp_range, limit=10)
    for i, item in enumerate(results['items']):
        print(i, item['name'], item['genres'])
        #print(i, item['name'], '//', item['artists'][0]['name'])
    print()
    
#%%
#Gets a lot of genres from the long-range parameter

def get_longterm_genres(limit):
    results = sp.current_user_top_artists(time_range='long_term', limit=limit)
    for i, item in enumerate(results['items']):
        print(i, item['name'], item['genres'])
        #print(i, item['name'], '//', item['artists'][0]['name'])
    return results

#makes a list of lists. Each item is a list of genre tags. One list per band
spam = [i['genres'] for i in results['items']]

#flattens that list of lists into one big list, with repeats
flat_list = []
for sublist in spam:
    for item in sublist:
        flat_list.append(item)
        
