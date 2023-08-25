import getpass
import sys

from github import BadCredentialsException, Github

from ..utils import delete_auth_token, set_auth_token


def login(option, opt_str, value, parser):
    print(
        "Please enter your github access token to login with your GitHub account:\n"
    )
    token = getpass.getpass(prompt="Token: ")

    try:
        gh = Github(token)
    except BadCredentialsException:
        print("Invalid token. Please try again.")

        sys.exit(1)

    username = gh.get_user().login

    set_auth_token(token)

    print(f"\nSuccessfully logged into {username}'s account!")


def logout(option, opt_str, value, parser):
    delete_auth_token()

    print(f"\nLogged out successfully!")
