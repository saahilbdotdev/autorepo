from github import Github, BadCredentialsException
from pathlib import Path
import sys
import json
import getpass


def getToken():
    try:
        f = open(f"{Path.home()}/.config/autorepo/creds.json", "r")
        creds = json.load(f)
        f.close()

        try:
            token = creds['token']
        except KeyError:
            print("Please login to your github account using the -l flag.")
            sys.exit(1)

        return token

    except FileNotFoundError:
        print("Please login to your github account using the -l flag.")
        sys.exit(1)


def login(option, opt_str, value, parser):
    print("Please enter your github access token to login with your GitHub account:\n")
    token = getpass.getpass(prompt="Token: ")

    try:
        gh = Github(token)
    except BadCredentialsException:
        print("Invalid token. Please try again.")
        sys.exit(1)

    f = open(f"{Path.home()}/.config/autorepo/creds.json", "w")
    json.dump({"token": token}, f, indent=2)
    f.close()

    print(f"\nSuccessfully logged into {gh.get_user().login}'s account.")
