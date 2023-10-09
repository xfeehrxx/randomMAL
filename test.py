import requests as req
import json
config = json.load(open('config.json'))


hdr={
    'X-MAL-CLIENT-ID' : config['clientId']
}

def animeList(user):
    with req.get('https://api.myanimelist.net/v2/users/' + user  + '/animelist?status=completed&limit=500&fields=list_status', headers=hdr) as r:
        anime = []
        for node in json.loads(r.text)['data']:
            if(node['list_status']['score'] < 6):
                  continue
            anime.append({'title' : node['node']['title'], 'score': node['list_status']['score']})
    return anime


mainUser = animeList(config['user'])
secondaryUser = animeList(config['user2'])

print('Encerrado.')

