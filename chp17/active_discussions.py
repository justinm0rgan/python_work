from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts, links, comments, labels = [], [], [], []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'by': response_dict['by'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    user_name = submission_dict['by']
    link_url = submission_dict['hn_link']
    link = f"<a href='{link_url}'>{user_name}</a>"
    links.append(link)

    owner = submission_dict['by']
    title = submission_dict['title']
    label = f"{owner}<br />{title}"
    labels.append(label)

    comment = {submission_dict['comments']}
    comments.append(comment)


# Make visualizaqtion
data = [{
    'type': 'bar',
    'x': links,
    'y': comments,
    'hovertext': labels,
    'marker':{
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': f'Top 30 active discussions on Hacker News',
    'titlefont': {'size': 28},
    'xaxis':{
        'title': 'Discussions',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis':{
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename= './output/top_30_active_discussions_hn.html') 