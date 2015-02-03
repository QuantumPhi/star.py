import requests, json
from getpass import getpass
from os.path import expanduser
from os.path import isfile

def authorize(user, pass):
    payload = { }
    r = requests.get("https://api.github.com/authorizations", """something""")
    if(!isfile(expanduser("~/.unstar"))):
        f = open(expanduser("~/.unstar/auth_token"))

    header = { "content-type": "application/vnd.github.mirage-preview+json" }

def toggle(user, repo):
    payload = { }
    header = { }
    r = requests.get()
