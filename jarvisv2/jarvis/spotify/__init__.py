import requests
import base64
import threading
import time
from spotify import config, spotify_client

# def get_user_auth():
#     scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
#     scopes = scopes.replace(" ", "%20")
    
#     url = f"https://accounts.spotify.com/authorize?response_type=code&client_id={config.SPOTIFY_CLIENT_ID}&scope={scopes}&redirect_uri=http://127.0.0.1:8888/callback"
#     webbrowser.open(url)

# def get_token():
#     url = "https://accounts.spotify.com/api/token"
#     headers = {
#         "Authorization": "Basic " + base64.b64encode((config.SPOTIFY_CLIENT_ID + ":" + config.SPOTIFY_CLIENT_SECRET).encode("ascii")).decode("ascii")
#     }
#     form = {
#         "grant_type": "authorization_code",
#         "code": config.SPOTIFY_AUTHORIZATION_CODE,
#         "redirect_uri": "http://127.0.0.1:8888/callback"
#     }

#     response = requests.post(url=url, headers=headers, data=form, json=True)
#     if (response.status_code == 200):
#         print(response.json())
#         config.SPOTIFY_ACCESS_TOKEN = response.json()["access_token"]
#     else:
#         print("Failure fetching Spotify Authorization Code: " + response.content.decode("ascii"))
#         exit()

# get_user_auth()
# init_token()

def refresh_token():
    url = "https://accounts.spotify.com/api/token"
    credentials = f"{config.SPOTIFY_CLIENT_ID}:{config.SPOTIFY_CLIENT_SECRET}"
    headers = {
        "Authorization": "Basic " + base64.b64encode(credentials.encode("ascii")).decode("ascii")
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": config.SPOTIFY_REFRESH_TOKEN
    }

    response = requests.post(url, headers=headers, data=data)

    if response.ok:
        config.SPOTIFY_ACCESS_TOKEN = response.json()["access_token"]

refresh_token()

def cache():
    while True:
        spotify_client.cache_device_ids()
        time.sleep(5)

threading.Thread(target=cache, daemon=True).start()
