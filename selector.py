import json
import requests as req
from datetime import datetime as dt
config = json.load(open('config.json'))

hdr = {
    'X-MAL-CLIENT-ID' : config['clientId']
    }

def animeValidation(a = {'id1', 'id2'}):
        with req.get('https://api.myanimelist.net/v2/anime/' + str(a[0]['id1']) + '?fields=end_date,synopsis,status, related_anime', headers=hdr) as r:
            dt1 = json.loads(r.text)['end_date']
            dt1 = dt.strptime(dt1,'%Y-%m-%d').date()

        with req.get('https://api.myanimelist.net/v2/anime/' + str(a[0]['id2']) + '?fields=end_date,synopsis,status, related_anime', headers=hdr) as r:
            dt2 = json.loads(r.text)['end_date']
            dt2 = dt.strptime(dt2,'%Y-%m-%d').date()

        if (dt1 == min([dt1, dt2])):
            return a[0]['id2']
        else:
             return a[0]['id1']

animes = []
with req.get('https://api.myanimelist.net/v2/users/' + config['user'] + '/animelist?status=plan_to_watch&limit=500', headers=hdr) as r:
    for node in json.loads(r.text)['data']:
        animes.append({'title' : node['node']['title'], 'id' : node['node']['id']})

x  = []
for anime in animes:
    for i in range(1, len(animes)):
        if(anime['title'].split(' ')[0] == animes[i]['title'].split(' ')[0]):
            x.append({'id1': anime['id'], 'id2': animes[i]['id']})
            v = animeValidation(x)  
            if(anime['id'] == v):
                animes.remove(anime)
            else:
                animes.remove(animes[i])
        break

    print('entrou')
      
    
print('Encerrado.')

