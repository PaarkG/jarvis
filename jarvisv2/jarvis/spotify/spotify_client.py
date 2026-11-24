import requests
from spotify import config

def get_profile():
    url = f"{config.SPOTIFY_BASE_URL}/me"
    response = requests.get(url=url, headers={"Authorization": get_access_token() })
    return response

def cache_device_ids():
    computer_id = get_computer_id()
    if computer_id != -1:
        config.SPOTIFY_COMPUTER_ID = computer_id

    phone_id = get_phone_id()
    if phone_id != -1:
        config.SPOTIFY_PHONE_ID = phone_id

def get_computer_id():
    resp = get_active_devices()
    devices = resp["devices"]

    for i in range(len(devices)):
        if devices[i]["type"] == "Computer":
            return devices[i]["id"]

    return -1

def get_phone_id():
    resp = get_active_devices()
    devices = resp["devices"]

    for i in range(len(devices)):
        if devices[i]["type"] == "Smartphone":
            return devices[i]["id"]

    return -1

def get_active_devices():
    url = f"{config.SPOTIFY_BASE_URL}/me/player/devices"

    response = requests.get(url=url, headers={"Authorization": get_access_token() })
    return response.json()

def start_playback_phone():
    return transfer_playback(config.SPOTIFY_PHONE_ID)

def start_playback_computer():
    return transfer_playback(config.SPOTIFY_COMPUTER_ID)

def start_playback(device_id = ""):
    url = f"{config.SPOTIFY_BASE_URL}/me/player/play?"
    if device_id != "":
        url = url + f"?device_id={device_id}"
    response = requests.put(url=url, headers={ "Authorization": get_access_token() })
    return response.ok

def stop_playback():
    url = f"{config.SPOTIFY_BASE_URL}/me/player/pause"
    response = requests.put(url=url, headers={ "Authorization": get_access_token() })
    return response.ok

def transfer_playback(device_id):
    url = f"{config.SPOTIFY_BASE_URL}/me/player"
    response = requests.put(url=url, headers={ "Authorization": get_access_token(), "Content-Type": "application/json" }, json={"device_ids": [ device_id ], "play": True})
    return response.ok

def next_song():
    url = f"{config.SPOTIFY_BASE_URL}/me/player/next"
    response = requests.post(url=url, headers={ "Authorization": get_access_token() })
    return response.ok

def previous_song():
    url = f"{config.SPOTIFY_BASE_URL}/me/player/previous"
    response = requests.post(url=url, headers={ "Authorization": get_access_token() })
    return response.ok


def get_access_token():
    return "Bearer " + config.SPOTIFY_ACCESS_TOKEN