# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey, Table

from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

#%%

daily_top20_tracks = Table(

    "daily_top20_tracks",

    Base.metadata,

    Column("author_id", Integer, ForeignKey("author.author_id")),

    Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),

)