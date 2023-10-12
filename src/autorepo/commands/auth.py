import getpass

import click
from github import BadCredentialsException, Github

from ..utils import delete_auth_token, set_auth_token


@click.command(
    name="login",
    help="Log in to GitHub using a Personal Access Token"
)
def login_cmd():
    click.echo("Please enter your GitHub Personal Access Token")
    token = getpass.getpass(prompt="Token: ")

    try:
        gh = Github(token)
        username = gh.get_user().login
    except BadCredentialsException:
        click.echo("Invalid token", err=True)

        return

    set_auth_token(token)

    click.echo(f"Logged in as {username}")


@click.command(
    name="logout",
    help="Log out of GitHub"
)
def logout_cmd():
    delete_auth_token()

    click.echo("Logged out")
