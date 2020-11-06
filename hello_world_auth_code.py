#! python
import sys
import spotipy
from config import username
from spotipy.oauth2 import SpotifyOAuth
#from collections import Counter


scope = 'user-top-read'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=username))

ranges = ['short_term', 'medium_term', 'long_term']

#inp = input("Enter an Artist ID")

if len(sys.argv) > 1:
    print(sys.argv[1])
    print(', '.join(sp.artist(sys.argv[1])['genres']))
    
else:
    inp = input("Enter an Artist ID:\n")
    sys.stdout.write(', '.join(sp.artist(inp)['genres']))