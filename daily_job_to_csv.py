# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:38:57 2020

@author: flamb
"""


from Authorization_Code import get_user_top_tracks_artists
from datetime import datetime

daily_top_20 = get_user_top_tracks_artists()
today_date = datetime.now().strftime("%d%b%Y")


daily_top_20.to_csv(f'CSVs/{todays_date}')