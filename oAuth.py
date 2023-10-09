import secrets 
import json
import requests as req
config = json.load(open('config.json'))

def get_new_code_verifier() -> str: 
    token = secrets.token_urlsafe(100)
    return token[:128]

def refresh_acess_token():
    url = " https://myanimelist.net/v1/oauth2/token"
    body ={
        "client_id": config['clientId'],
        "grant_type": "refresh_token",
        "refresh_token": config['refreshToken']
    }
    with req.post(url, data=body) as r:
        acess_token = r.text

print(refresh_acess_token())
        


