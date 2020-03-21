# Try using Plotly to make the visualization for a random walk.

import plotly.graph_objects as go

from refact_random_walk import Randomwalk

# Make a random walk.
rw = Randomwalk(50_000)
rw.fill_walk()

fig = go.Figure()

fig.add_trace(go.Scatter(x=rw.x_values, y=rw.y_values,
	mode='lines',
	name='lines'))

fig.layout.xaxis.visible=False
fig.layout.yaxis.visible=False
fig.update_layout(
	title={
        'text': "Results of random walk 50_000 times",
        'y':.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.show()