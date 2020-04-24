# To use this program enter the agruments as follows...
# python3 other_lang_repos_visual.py <LANGUAGE> <OUTPUT FILENAME>
#
# Example usage: 
# python3 other_lang_repors_visual.py python python_repos.html

import requests
import sys

from plotly.graph_objs import Bar
from plotly import offline

language = sys.argv[1]
output_filename = sys.argv[2]

# Make an API call and store the response.
url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
	repo_name = repo_dict['name']
	repor_url = repo_dict['html_url']
	repo_link = f"<a href='{repor_url}'>{repo_name}</a>"
	repo_links.append(repo_link)
	stars.append(repo_dict['stargazers_count'])

	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner}<br />{description}"
	labels.append(label)

# Make visuulization.
data = [{
	'type': 'bar',
	'x': repo_links,
	'y': stars,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(60, 100, 150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
	'opacity': 0.6,
}]

my_layout = {
	'title': f'Most-Starred {language.title()} Projects on Github',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Stars',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename= './output/' + output_filename)