import requests, json

def authorize(user, pass):
    payload = { "" }
    header = { "content-type": "application/vnd.github.mirage-preview+json" }
    r = requests.get("https://api.github.com/authorizations", )
