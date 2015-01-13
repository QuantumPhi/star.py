import requests, json

def authenticate(user, pass, auth):
    payload = { '' }
    header = { 'content-type': 'application/vnd.github.mirage-preview+json' }
