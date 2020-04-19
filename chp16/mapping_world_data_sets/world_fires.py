#!/usr/bin/env python3
"""This program will map world fires using plotly over a 7 day period"""
import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get lat/lon and brightness from file and append to list
    lons, lats, brights = [], [], []
    for row in reader:
            lons.append(float(row[1]))
            lats.append(float(row[0]))
            brights.append(float(row[2]))
    print(lons[:10])

# # Map the world fires.
# data = [{
#     'type': 'scattergeo',
#     'lon': lons,
#     'lat': lats,
#     # 'text': hover_texts,
#     'marker': {
#         'size': brights,
#         'color': brights,
#         'colorscale': 'Reds',
#         'reversescale': False,
#         'colorbar': {'title': 'Brightness'},
#     },
# }]

# # Automate the map title
# title = "World Fires 7 day"
# my_layout = Layout(title=title)

# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='world_fires_7_day.html')
