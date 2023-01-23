import json
import requests as req
import random 
config = json.load(open('config.json'))
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
    
next = ''
i = 0
print(Fore.BLUE, 'WARNING: You have ONLY 3 CHANCES to choose an anime. Good luck and remember, this is your own plan to watch list!')
while next != 'N' and i !=3 :
    anime = random.choice(list(animes))
    print("Your selected anime was: \n " + Fore.WHITE, anime['title'] + Fore.BLUE, '\n Synopsis: \n ' + Fore.WHITE, anime['synopsis'], Fore.YELLOW)
    next = input('Enter Y if you want to try again, otherwise enter N: ')
    i +=1
    animes.remove(anime)

if i == 3:
    print(Fore.BLUE, "Well, too bad, you were warned. Only 3 chances. \n Your last one will be the one since you want to be pick in a RANDOM ANIME SELECTOR.")

#Tentar encontrar o anime no Anihub
title = anime['title'].replace(' ', '-').replace(':', '').replace('!', '').replace('(TV)', '').lower()
link = 'https://anihub.tv/anime/' + title + '/' 
with req.get(link) as r:
    if (r.status_code != 200):
        print(Fore.BLUE, 'We could not find this anime on Anihub, but good luck!')
    else:
        print(Fore.BLUE, 'Here it is a link you could try to watch it on: \n' + Fore.MAGENTA, link)

print(Fore.BLUE, "That's it. Go watch anime. Come back for more suggestions!")

