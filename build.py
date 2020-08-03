import requests

REPOS = 'tuot/Notes'


url = 'https://api.github.com/{}/Notes/issues'.format(REPOS)
res = requests.get(url)

print(res['body'])