# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:44:44 2020
I'm hitting hard, oh word, I'm gon rock it
Once the shit drops, that's dough to the pocket
@author: flamb
"""

from Authorization_Code import get_user_top_tracks_artists
import sqlite3

#%% Connect to database. Print some boring shit.

try:
    sqliteConnection = sqlite3.connect('spotify.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()
    
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
        
 
#%% Connect to database, SELECT *

def print_db_info(table_name):
    sqliteConnection = sqlite3.connect('spotify.db')
    cursor = sqliteConnection.cursor()
    
    sqlite_Query = "select * table_name;"
    cursor.execute(sqlite_Query)
    print(cursor.fetchall())
    cursor.close()
        
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
            
#%% Create the table that will hold the daily top 20 chart dumps
        
try:
    sqliteConnection = sqlite3.connect('spotify.db')
    sqlite_create_table_query = '''CREATE TABLE daily_top20_tracks (
                                id INTEGER PRIMARY KEY,
                                position TEXT NOT NULL,
                                art_id TEXT NOT NULL,
                                art_name TEXT NOT NULL,
                                album_name TEXT NOT NULL,
                                song_id TEXT NOT NULL,
                                song_name TEXT NOT NULL,
                                popularity TEXT NOT NULL,
                                date datetime);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")
        
#%% Insert a song into the database

# todays_top_20 = get_user_top_tracks_artists()
# todays_top_20.iloc[0].to_dict()

try:
    sqliteConnection = sqlite3.connect('spotify.db')
    cursor = sqliteConnection.cursor()
    print('Successfully Connected to SQLite')

    sqlite_insert_query = """INSERT INTO daily_top20_tracks
                            (id, position, art_id, art_name, album_name, song_id, song_name, popularity, date)
                            VALUES
                            (0, 3, '6Nwhmo3adbTqPMCsgBgkf4', 'Slothrust', 'Of Course You Do', '4IvPEuTkgfHfDQIxcwfcZ0', 'Cubicle', 33, '12-Dec-2020')"""
                        
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")

#%%DROP DUPLICATE ARTISTS ROWS
        
try:
    sqliteConnection = sqlite3.connect('spotify.db')
    cursor = sqliteConnection.cursor()

    query = """ DELETE FROM artists WHERE rowid NOT IN (SELECT min(rowid) FROM artists GROUP BY art_id) """

    cursor.execute(query)
    
    select_query = (''' SELECT * FROM artists''')
    cursor.execute(query)
    blob = cursor.fetchall()
    
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

#%% RETURN THE LIST OF UNIQUE ARTIST NAMES IN THE ARTISTS Table
def get_artists_from_db():
    try:
        sqliteConnection = sqlite3.connect('spotify.db')
        select_query = (''' SELECT DISTINCT art_name FROM artists''')
        cursor = sqliteConnection.cursor()
        cursor.execute(select_query)
        records = cursor.fetchall()
        
    except sqlite3.Error as error:
        print("Something went wrong", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return([i[0] for i in records])
        
#%% Create the table that will hold the daily top 20 artists dumps
        
try:
    sqliteConnection = sqlite3.connect('spotify.db')
    sqlite_create_table_query = '''CREATE TABLE daily_top20_artists (
                                id INTEGER PRIMARY KEY,
                                position TEXT NOT NULL,
                                art_id TEXT NOT NULL,
                                art_name TEXT NOT NULL,
                                popularity INT NOT NULL,
                                followers INT NOT NULL,
                                date datetime);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")