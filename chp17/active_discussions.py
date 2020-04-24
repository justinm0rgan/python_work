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
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")


# Make visualizaqtion
data = [{
    'type': 'bar',
    'x':,
    'y':,
    'hovertext':,
    'marker':{
        'color':,
        'line':,
    },
    'opacity':,
}]

my_layout = {
    'title':,
    'titlefont':,
    'xaxis':{
        'title':
        'titlefont':
        'tickfont':,
    },
    'yaxis':{
        'title':,
        'titlefont':,
        'tickfont':,
    },
}

fig = {'data': data, 'my_layout': my_layout}
offline.plot(fig, filename='./output/most_active_discussions_hn.html'