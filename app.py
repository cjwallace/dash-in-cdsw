# # Dash

# ## Setup

# We must ensure the experiment container has the dependencies it needs,
# so we inline install dash.

!pip3 install dash

# There are a couple of dependencies we need for the CDSW end of things.

import os
from IPython.display import HTML

# ## Define Dash app

# And then there are the dependencies for the Dash bits.
# This script is taken from the Dash getting started guide
# [here](https://dash.plot.ly/getting-started).

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
  
    html.Div(children='''
        Dash: but on CDSW.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


# ## Serve

# Print the url of the hosted app

print('Dash starting at {}.{}'.format(
          os.environ['CDSW_ENGINE_ID'],
          os.environ['CDSW_DOMAIN']))

# And provide a link

HTML("<a href='https://{}.{}'>Open Dash</a>".format(
    os.environ['CDSW_ENGINE_ID'],
    os.environ['CDSW_DOMAIN']
))

# Then run the server

app.run_server(host=os.environ['CDSW_IP_ADDRESS'],
               port=int(os.environ['CDSW_PUBLIC_PORT']))