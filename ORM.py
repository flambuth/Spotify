# -*- coding: utf-8 -*-
'''
Some roads are only seen at night.
Ghost roads, nothing but neon signs.
'''
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()

daily_top20_tracks= Table(
    "daily_top20_tracks",
    Base.metadata,
    ID = Column(Integer, primary_key=True)
    position = Column(Integer, primary_key=True)
    art_id = Column(Integer),
    art_name = Column(String(250)),
    album_name = Column(String(250)),
    song_id = Column(String(250)),
    song_name = Column(String(250)),
    popularity = Column(Integer),
    date  = Column(String(250))
)
    
artists= Table(
    "artitss",
    Base.metadata,
    ID = Column(Integer)
    art_id = Column(Integer, primary_key=True),
    art_name = Column(String(250)),
    followers = Column(String(250)),
    genre = Column(Integer),
    popularity  = Column(String(250))
    first_release  = Column(String(250))
    query_date = Column()
)
    
'''
CREATE TABLE artists (
                                    id INTEGER PRIMARY KEY,
                                    art_id TEXT NOT NULL,
                                    art_name TEXT NOT NULL,
                                    followers INTEGER NOT NULL,
                                    genre STRING NOT NULL,
                                    popularity TEXT NOT NULL,
                                    album_count INTEGER NOT NULL,
                                    first_release TEXT NOT NULL,
                                    query_date TEXT NOT NULL);'''