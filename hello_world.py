#! python
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

inp = input("Enter an Artist ID")

if len(sys.argv) > 1:
    print(sys.argv[1])
    print(', '.join(sp.artist(sys.argv[1])['genres']))
    counter = input('Do you want to look up another artist? \n 0 for yes')
    
else:
    inp = input("Enter an Artist ID:\n")
    sys.stdout.write(', '.join(sp.artist(inp)['genres']))
    counter = input('Do you want to look up another artist? \n 0 for yes')