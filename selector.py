import json
import requests as req
import random 
config = json.load(open('config.json'))
import colorama
from colorama import Fore 



hdr = {
    'X-MAL-CLIENT-ID' : config['clientId']
    }

animes = []
with req.get('https://api.myanimelist.net/v2/users/' + config['user'] + '/animelist?status=plan_to_watch&limit=500&fields=synopsis', headers=hdr) as r:
    for node in json.loads(r.text)['data']:
        animes.append({'title' : node['node']['title'], 'id' : node['node']['id'], 'synopsis': node['node']['synopsis']})

x  = []
for anime in animes: #remoção de animes que começam com a mesma palavra para eliminar temporadas do mesmo anime e reduzir a lista
    i = list(animes).index(anime) + 1
    if (i == len(animes)):
        break
    while anime['title'].split(' ')[0] == animes[i]['title'].split(' ')[0]:
        animes.remove(animes[i])

print('Encerrado.')

