#! /usr/bin/env python

import requests, json
from getpass import getpass as gp
from os import makedirs as mk
from os.path import isfile as isf, exists, expanduser as eu
from sys import argv

def print_help():
    print("Usage: python toggle.py [user] [repo]")

def authorize():
    if not exists(eu("~/.unstar/auth_token")):
        # TODO: clean up code
        user = raw_input("Username: ")
        pswd = gp("Password: ")
        headers = { "content-type": "application/vnd.github.mirage-preview+json" }
        payload = { "note": "star.py", "scopes": "repo" }
        r = requests.post("https://api.github.com/authorizations", auth = (user, pswd), headers = headers, data = json.dumps(payload))
        if(r.status_code == 401) and ("X-GitHub-OTP" in r.headers):
            otp = input("OTP/2FA code: ")
            headers["X-GitHub-OTP"] = str(otp)
            r = requests.post("https://api.github.com/authorizations", auth = (user, pswd), headers = headers, data = json.dumps(payload))
        token = r.json()["token"]
        if not exists(eu("~/.unstar")):
            mk(eu("~/.unstar"))
        f = open(eu("~/.unstar/auth_token"), "w")
        f.write("%s" % token)
        return token
    else:
        return open(eu("~/.unstar/auth_token"), "r").read()


def toggle(token, split):
    split = split.split("/")
    user, repo = split[0], split[1]
    headers = { "content-type": "application/vnd.github.mirage-preview+json", "Authorization": "token %s" % token }
    payload = { }
    r = requests.get("https://api.github.com/user/starred/" + user + "/" + repo, headers = headers, data = json.dumps(payload))
    if r.status_code == 404:
        r = requests.put("https://api.github.com/user/starred/{0}/{1}".format(user, repo), headers = headers, data = json.dumps(payload))
        print "%s %s" % (r.status_code, r.reason)
    elif r.status_code == 204:
        r = requests.delete("https://api.github.com/user/starred/{0}/{1}".format(user, repo), headers = headers, data = json.dumps(payload))
        print "%s %s" % (r.status_code, r.reason)

token = authorize()
if len(argv) != 2:
    print_help()
else:
    toggle(token, argv[1])
