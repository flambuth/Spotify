#import sqlite3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#from datetime import datetime
from config import username

#scope is narrowed just to what the 'user/me' has recently played.
def last_song_played():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, scope='user-read-recently-played'))

    spotify_request = sp.current_user_recently_played(limit=1)
    last_song = spotify_request['items'][0]
    artist_name = last_song['track']['artists'][0]['name']
    song_name =  last_song['track']['name']
    song_link = last_song['track']['external_urls']['spotify']
    last_played = last_song['played_at']

    return dict(art_name=artist_name, song_name=song_name, song_link=song_link, last_played=last_played)