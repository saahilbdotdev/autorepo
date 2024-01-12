import getpass

import click
from github import BadCredentialsException, Github

from autorepo.utils import (add_user, delete_auth_token, get_current_user,
                            remove_user, set_auth_token, set_current_user,
                            set_default_current_user, token_exists)


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

    set_auth_token(username, token)

    click.echo(f"Logged in as {username}")

    add_user(username)
    set_current_user(username)

    click.echo(f"{username} is now the current user")


@click.command(
    name="logout",
    help="Log the current user out of GitHub"
)
def logout_cmd():
    current_user = get_current_user()

    if not current_user:
        click.echo("You are not logged in to any GitHub account", err=True)

        return

    delete_auth_token(current_user)
    remove_user(current_user)
    set_default_current_user()

    click.echo(f"Logged out of {current_user}")


@click.command(
    name="current-user",
    help="Show the current GitHub user"
)
def current_user_cmd():
    current_user = get_current_user()
    if not current_user:
        click.echo("You are not logged in to any GitHub account", err=True)

        return

    click.echo(current_user)


@click.command(
    name="switch-user",
    help="Switch the current GitHub user"
)
@click.argument("username", required=True)
def switch_user_cmd(username):
    if not token_exists(username):
        click.echo(
            f"Please enter your GitHub Personal Access Token for {username}"
        )
        token = getpass.getpass(prompt="Token: ")

        try:
            gh = Github(token)
            username = gh.get_user().login
        except BadCredentialsException:
            click.echo("Invalid token", err=True)

            return

        set_auth_token(username, token)
        add_user(username)

        click.echo(f"Logged in as {username}")

    set_current_user(username)

    click.echo(f"Switched to {username} as the current user")
