import requests, json
from getpass import getpass
from os.path import expanduser
from os.path import isfile

def authorize():
    if(not(isfile(expanduser("~/.unstar")))):
        user = raw_input("Username: ")
        pswd = getpass("Password: ")
        headers = { "content-type": "application/vnd.github.mirage-preview+json" }
        payload = { "note": "star and unstar repositories from CLI" }
        r = requests.get("https://api.github.com/authorizations", auth=(user, pswd), headers = headers, data=json.dumps(payload))
        if(r.status_code == 401) and ("X-GitHub-OTP" in r.headers):
            print(r.headers.get("X-GitHub-OTP"))
        # f = open(expanduser("~/.unstar/auth_token"))

def toggle(user, repo):
    payload = { }
    header = { }
    r = requests.get()

authorize()
