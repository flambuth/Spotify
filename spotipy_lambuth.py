# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 21:22:00 2020

@author: flamb
"""
# Shows the top tracks for a user

import spotipy
#import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth


scope = 'user-top-read'
username = 'lambuth'
client_id = '0'
client_secret = '0'
redirect_uri = 'http://localhost:8888'

#token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

#sp = spotipy.Spotify(token)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username='lambuth'))

ranges = ['short_term', 'medium_term', 'long_term']

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_artists(time_range=sp_range, limit=10)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
    print()
#%%    
   
    
    
#%%
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
    
#%%

import spotipy
import spotipy.util as util
 
scope = 'user-read-currently-playing'
# scope = 'user-read-playback-state'
# works as well

username = 'lambuth'
client_id = 'e651edc8caf94abcbac8ee3faaca3236'
client_secret = '7daf8f754d874d4689db554df936d845'
redirect_uri = 'http://localhost:8888'

token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

spotify = spotipy.Spotify(auth=token)
current_track = spotify.current_user_playing_track()

print(current_track)
    