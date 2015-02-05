import requests, json
from getpass import getpass as gp
from os import makedirs as mk
from os.path import isfile as isf, exists, expanduser as eu


def authorize():
    if not exists(eu("~/.unstar/auth_token")):
        # TODO: clean up code
        user = raw_input("Username: ")
        pswd = gp("Password: ")
        headers = { "content-type": "application/vnd.github.mirage-preview+json" }
        payload = { "note": "unstar", "scopes": "repo" }
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


def toggle(token, user, repo):
    headers = { "content-type": "application/vnd.github.mirage-preview+json", "Authorization": "token %s" % token }
    payload = { }
    r = requests.get("https://api.github.com/user/starred/" + user + "/" + repo, headers = headers, data = json.dumps(payload))
    print r.status_code

token = authorize()
toggle(token, "foo", "bar")
