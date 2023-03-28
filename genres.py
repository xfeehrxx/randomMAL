import json
import requests as req
from collections import Counter
import matplotlib.pyplot as plt
config = json.load(open('config.json'))

hdr = {
    'X-MAL-CLIENT-ID' : config['clientId']
    }

animes = []

with req.get('https://api.myanimelist.net/v2/users/' + config['user']  + '/animelist?status=completed&limit=500&fields=genres,list_status', headers=hdr) as r:
        for node in json.loads(r.text)['data']:
            if(node['list_status']['score'] < 8):
                  continue
            animes.append({'title' : node['node']['title'], 'genres': node['node']['genres']})
genres = []

for anime in animes:
      for genre in anime['genres']:
            genres.append({'genre': genre['name']})
gen = Counter(map(lambda x: x['genre'], genres))
gen = dict(gen.most_common()[:10])

plt.bar(gen.keys(), gen.values())
plt.title("top 10 generos de animes aprovados")
plt.xlabel("Generos")
plt.ylabel("Frequência")
plt.show()
print('Encerrado.')

