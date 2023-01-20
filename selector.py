import json
import requests as req
from datetime import datetime as dt
config = json.load(open('config.json'))

hdr = {
    'X-MAL-CLIENT-ID' : config['clientId']
    }

animes = []
with req.get('https://api.myanimelist.net/v2/users/' + config['user'] + '/animelist?status=plan_to_watch&limit=500', headers=hdr) as r:
    for node in json.loads(r.text)['data']:
        animes.append({'title' : node['node']['title'], 'id' : node['node']['id']})

x  = []
for anime in animes:
    for i in range(list(animes).index(anime) + 1, len(animes)):
        if(anime['title'].split(' ')[0] == animes[i]['title'].split(' ')[0]):
            animes.remove(animes[i])
            i -=1
        else:
            break
      
    
print('Encerrado.')

