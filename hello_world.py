#! python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

inp = input("Enter an Artist ID")

sys.stdout.write(', '.join(sp.artist(inp)['genres']))