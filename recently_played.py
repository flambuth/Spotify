#import sqlite3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#from datetime import datetime

from config import username

#scope is narrowed just to what the 'user/me' has recently played.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, scope='user-read-recently-played'))

spotify_request = sp.current_user_recently_played(limit=1)

last_song = spotify_request['items'][0]['track']

artist_name = last_song['artists'][0]['name']
song_name =  last_song['name']
song_link = last_song['external_urls']['spotify']
