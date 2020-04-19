import json
import requests
from requests.exceptions import HTTPError

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
response = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson')
response.raise_for_status()
jsonResponse = response.json()
# filename = 'data/eq_data_30_day_m1.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)

all_eq_dicts = jsonResponse['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])


# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Cividis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

# Automate the map title
title = jsonResponse['metadata']['title']
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_sig_month.html')
