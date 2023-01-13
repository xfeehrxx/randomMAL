import json
import requests as req
config = json.load(open('config.json'))

hdr = {
    'X-MAL-CLIENT-ID' : config['clientId']
    }

def animeValidation(a = {'id', 'title'}):
 with req.get('https://api.myanimelist.net/v2/anime/' + str(16498) + '?fields=start_date,end_date,synopsis,status, related_anime', headers=hdr) as r:
    # for i in range(len(json.loads(r.text)['related_anime'])):
    #     line = json.loads(r.text)['related_anime'][i]['relation_type']
    #     if (line == 'prequel' | line == 'sequel'):
    print(r.text)
    


animes = []
with req.get('https://api.myanimelist.net/v2/users/' + config['user'] + '/animelist?status=plan_to_watch&limit=500', headers=hdr) as r:
    for node in json.loads(r.text)['data']:
        animes.append({'title' : node['node']['title'], 'id' : node['node']['id']})

for anime in animes:
    animeValidation(anime)
    print('Encerrado.')