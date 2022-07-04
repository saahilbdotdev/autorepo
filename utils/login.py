from github import Github, BadCredentialsException
from pathlib import Path
import sys
import json
import getpass

credsPath = Path(f"{Path.home()}/.config/autorepo/creds.json")


def getToken():
    global credsPath

    if credsPath.exists():
        f = credsPath.open("r")
        creds = json.load(f)
        f.close()

        try:
            token = creds['token']
        except KeyError:
            print("Please login to your github account using the -l flag.")
            sys.exit(1)

        return token
    else:
        print("Please login to your github account using the -l flag.")
        sys.exit(1)


def login(option, opt_str, value, parser):
    global credsPath

    print("Please enter your github access token to login with your GitHub account:\n")
    token = getpass.getpass(prompt="Token: ")

    try:
        gh = Github(token)
    except BadCredentialsException:
        print("Invalid token. Please try again.")
        sys.exit(1)

    f = credsPath.open("w")
    json.dump({"token": token}, f, indent=2)
    f.close()

    print(f"\nSuccessfully logged into {gh.get_user().login}'s account.")
