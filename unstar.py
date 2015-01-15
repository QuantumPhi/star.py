import requests, json

def authorize(user, pass):
    payload = { }
    header = { "content-type": "application/vnd.github.mirage-preview+json" }
    r = requests.get("https://api.github.com/authorizations", """something""")

def toggle(user, repo):
    payload = { }
    header = { }
    r = requests.get()
