# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:56:09 2020
I wrote this module first. It probably can do with some refactoring.

Tú me dejaste de querer cuando te necesitaba
Cuando más falta hacía tú me diste la espalda
    
ranges = 
    long_term (calculated from several years of data and including all new data as it becomes available), 
    medium_term (approximately last 6 months), 
    short_term (approximately last 4 weeks)
"""
import pandas as pd
import spotipy
from config import username
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime


#I think scope is asked once and only once. After being granted a scope request
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username))

ranges = ['short_term', 'medium_term', 'long_term']

#%%


def get_top_artists(time_range='short_term', limit=20):
    
    cols = ['art_id', 'art_name', 'popularity', 'followers']
    
    x = sp.current_user_top_artists(time_range=time_range, limit=limit)
    
    art_id = [i['id'] for i in x['items']]
    art_name = [i['name'] for i in x['items']]
    popularity = [i['popularity'] for i in x['items']]
    followers = [i['followers']['total'] for i in x['items']]
    
    values = [art_id, art_name, popularity, followers]
    date = [datetime.now().strftime("%Y-%m-%d")]*20
    position = list(range(1,21))
    blob = dict(zip(cols, values))
    blob['position'] = position
    blob['date'] = date
    return blob    




#%% No Dataframes. Just Dictionaries
    
def get_daily_top20_tracks():
    '''
    Returns a dictionary of the top most played tracks in user's short term range
    '''
    x = sp.current_user_top_tracks(time_range='short_term')
    
    cols = ['art_id', 'art_name','album_name','song_id', 'song_name', 'popularity']
    
    
    art_id = [i['artists'][0]['id'] for i in x['items']]
    art_name = [i['artists'][0]['name'] for i in x['items']]
    album_name = [i['album']['name'] for i in x['items']]
    song_id = [i['external_urls']['spotify'][-22:] for i in x['items']]
    song_name = [sp.track(i)['name'] for i in song_id]
    popularity = [sp.track(i)['popularity'] for i in song_id]
    
    values = [art_id, art_name, album_name, song_id, song_name, popularity]
    
    blob = dict(zip(cols, values))
    date = [datetime.now().strftime("%Y-%m-%d")]*20
    position = list(range(1,21))
    blob['position'] = position
    blob['date'] = date
    return blob


#%% Just Dictionaries with genre tags added to the process
    
# def get_daily_top20_tracks_expanded():
#     '''
#     Returns a dictionary of the top most played tracks in user's short term range
#     '''
#     x = sp.current_user_top_tracks(time_range='short_term')
    
#     cols = ['art_id', 'art_name','album_name','song_id', 'song_name', 'popularity']
    
    
#     art_id = [i['artists'][0]['id'] for i in x['items']]
#     art_name = [i['artists'][0]['name'] for i in x['items']]
#     album_name = [i['album']['name'] for i in x['items']]
#     song_id = [i['external_urls']['spotify'][-22:] for i in x['items']]
#     song_name = [sp.track(i)['name'] for i in song_id]
#     popularity = [sp.track(i)['popularity'] for i in song_id]
    
#     values = [art_id, art_name, album_name, song_id, song_name, popularity]
    
#     blob = dict(zip(cols, values))
#     date = [datetime.now().strftime("%Y-%m-%d")]*20
#     position = list(range(1,21))
#     blob['position'] = position
#     blob['date'] = date
#     return blob



#%%
    
# def get_artist_top_ten_tracks(artist_id, country='US'):
#     '''
#     Returns a 2x10 dataframe of the top most played tracks from an artist. Probably
#     of all time.
       
#     Country set to default. Can only do one country at a time. Set the default for US.
#     Not sure what happens if country isn't set.
#     https://api.spotify.com/v1/artists/{id}/top-tracks
#     '''
#     x =  sp.artist_top_tracks(artist_id, country)
#     cols = ['song_id', 'song_name'] 
#     song_id = [track['uri'][-22:-1] for track in x['tracks']]
#     song_name = [sp.track(track['uri'])['name'] for track in x['tracks']]
#     values = [song_id,song_name]
#     return pd.DataFrame((dict(zip(cols, values))))
    
# def get_user_top_tracks_artists():
#     '''
#     Returns a 3x20 dataframe of the top most played tracks in user's short term range
#     '''
#     x = sp.current_user_top_tracks(time_range='short_term')
    
#     cols = ['art_id', 'art_name','album_name','song_id', 'song_name', 'popularity']
#     art_id = [i['artists'][0]['id'] for i in x['items']]
#     art_name = [i['artists'][0]['name'] for i in x['items']]
#     album_name = [i['album']['name'] for i in x['items']]
#     song_id = [i['external_urls']['spotify'][-22:] for i in x['items']]
#     song_name = [sp.track(i)['name'] for i in song_id]
#     song_popularity = [sp.track(i)['popularity'] for i in song_id]
#     values = [art_id,art_name,album_name,song_id, song_name, song_popularity]
    
#     blob = pd.DataFrame((dict(zip(cols, values))))
#     blob['date'] = datetime.now().strftime("%Y-%m-%d")
#     blob.reset_index(inplace=True)
#     blob = blob.rename(columns = {'index':'daily_position'})
#     blob['daily_position'] = blob['daily_position'] + 1
#     return blob

#%% Get songs in a playlist

# def playlist_songs(playlistID):
#     playlist = sp.playlist(playlistID)
    
#     tracks = [i for i in playlist['tracks']['items']]
#     song_names = [i['track']['name'] for i in tracks]
#     artists = [i['track']['artists'][0]['name'] for i in tracks]

#     return list(enumerate(zip(artists,song_names)))


#%% recent tracks

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, scope='user-read-recently-played'))

# def get_recent_tracks():
#     return sp.current_user_recently_played()












































#%%
#Gets top artist in 3 time ranges
# def print_user_top_artists_in_3_ranges():
#     ranges = ['short_term', 'medium_term', 'long_term']
#     for sp_range in ranges:
#         print("range:", sp_range)
#         results = sp.current_user_top_artists(time_range=sp_range, limit=10)
#         for i, item in enumerate(results['items']):
#    sp.         print(i, item['name'], item['genres'])
#             #print(i, item['name'], '//', item['artists'][0]['name'])
#         print()
        
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

def get_playlist_songs(playlist_id):
    """
    This is going to take a lot of data transfomrations. It's like 9 layers deep
    nested.
    
    """
    pass

        
