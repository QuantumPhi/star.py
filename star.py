#! /usr/bin/env python

import requests, json
from getpass import getpass as gp
from os import makedirs as mk
from os.path import isfile as isf, exists, expanduser as eu
from sys import argv

def print_help():
    print("Usage: python star.py [user]/[repo]")

def authorize(force = False):
    if not exists(eu("~/.unstar/auth_token")) or force:
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

def check(token, user, repo):
    headers = { "content-type": "application/vnd.github.mirage-preview+json", "Authorization": "token %s" % token }
    r = requests.get("https://api.github.com/user/starred/{0}/{1}".format(user, repo), headers = headers)
    if r.status_code == 204:
        return True
    elif r.status_code == 401:
        authorize(True)
    return False

def star(token, user, repo):
    headers = { "content-type": "application/vnd.github.mirage-preview+json", "Authorization": "token %s" % token }
    r = requests.put("https://api.github.com/user/starred/{0}/{1}".format(user, repo), headers = headers)
    if r.status_code == 204:
        print "starred %s/%s" % (user, repo)
    else:
        print "%s %s" % (r.status_code, r.reason)

def unstar(token, user, repo):
    headers = { "content-type": "application/vnd.github.mirage-preview+json", "Authorization": "token %s" % token }
    r = requests.delete("https://api.github.com/user/starred/{0}/{1}".format(user, repo), headers = headers)
    if r.status_code == 204:
        print "unstarred %s/%s" % (user, repo)
    else:
        print "%s %s" % (r.status_code, r.reason)

def toggle(token, user, repo):
    headers = { "content-type": "application/vnd.github.mirage-preview+json", "Authorization": "token %s" % token }
    payload = { }
    if check(token, user, repo):
        unstar(token, user, repo)
    else:
        star(token, user, repo)

token = authorize()
if len(argv) != 2:
    print_help()
else:
    arg = argv[1].split("/")
    user, repo = arg[0], arg[1]
    toggle(token, user, repo)
