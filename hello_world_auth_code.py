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
counter = 0
inp = input("Enter an Artist ID")

#while counter == 0:
if len(sys.argv) > 1:
    print(sys.argv[1])
    print(', '.join(sp.artist(sys.argv[1])['genres']))
    counter = input('Do you want to look up another artist? \n 0 for yes')
    
else:
    inp = input("Enter an Artist ID:\n")
    sys.stdout.write(', '.join(sp.artist(inp)['genres']))
    counter = input('Do you want to look up another artist? \n 0 for yes')