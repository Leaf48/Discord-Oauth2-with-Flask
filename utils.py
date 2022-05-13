import json

import requests

with open("./config.json", mode="r") as f:
    CONFIG = json.load(f)


def get_token(code: str):
    data = {
        "client_id": CONFIG["client_id"],
        "client_secret": CONFIG["secret"],
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": CONFIG["redirect_URI"]
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    r.raise_for_status()
    print(r.json())
    return r.json()["access_token"]


def get_user_guilds(token: str):
    r = requests.get("%s/users/@me/guilds" % CONFIG["endpoint"], headers={"Authorization": f"Bearer {token}"})
    r.raise_for_status()
    return r.json()
