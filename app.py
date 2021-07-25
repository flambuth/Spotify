import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import sqlite3
from collections import Counter
import nltk

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)

app.layout = html.Div(html.H1)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
query_artists = 'select * from artists;'
conn = sqlite3.connect('spotify.db')
cursor = conn.cursor()
artists = cursor.execute(query_artists).fetchall()
genres_rawcount = [i[4] for i in artists]
genre_blob = ' '.join(genres_rawcount)
genre_wordlist = nltk.word_tokenize(genre_blob)
unigrams = Counter(genre_wordlist).most_common(10)
raw_grams = Counter(genres_rawcount).most_common(10)
df = pd.DataFrame(raw_grams, columns = ['genre','count'])
blob = df['genre'] == 'None'

df = df.loc[~blob]
fig = px.bar(df, x='genre', y='count', labels={'count':'Artists'})
#2nd fig
df2 = pd.DataFrame(unigrams, columns = ['genre','count'])
fig2 = px.bar(df2, x='genre', y='count', labels={'genre':'Words', 'count':'Frequency in genre tags'})


fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(children=[
    html.H1(children='Most Common Genre Tags in my listening data', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    html.Div(children='''
        Genre tag is the first one found among available genre tags pulled from the Spotify API
    ''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.H1(children='Most Common Words in Genre Tags', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.Div(children='''
        Genre tag is the first one found among available genre tags pulled from the Spotify API
    ''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)