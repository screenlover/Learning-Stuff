import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

stars = [repo_dict['stargazers_count'] for repo_dict in repo_dicts]
hover_texts = [f"{repo_dict['owner']['login']}<br>{repo_dict['description']}" for repo_dict in repo_dicts]
repo_links = [f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>" for repo_dict in repo_dicts]

title = "Most-Starred Python Projects on Github"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x = repo_links, y = stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.show()
