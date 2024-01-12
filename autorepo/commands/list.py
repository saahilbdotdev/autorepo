import click
from github import Github

from autorepo.utils import (get_auth_token, get_current_user,
                            list_gitignore_templates, list_licenses,
                            list_repositories, list_users)


@click.group(
    name="list",
    help="List artifacts from GitHub"
)
def list_group():
    pass


@click.command(
    name="users",
    help="List the users that have logged in to autorepo"
)
def users_cmd():
    users = list_users()

    if len(users) == 0:
        click.echo("No users have logged in to autorepo")

        return

    click.echo(f"{len(users)} user(s) have logged in to autorepo\n")
    click.echo("Users:")

    for i, user in enumerate(users):
        click.echo(f"{i+1}: {user}")


@click.command(
    name="licenses",
    help="List the licenses available on GitHub"
)
def licenses_cmd():
    if not get_current_user():
        click.echo(
            "You must be logged in to list licenses",
            err=True
        )

        return

    user = get_current_user()

    list_licenses(user)


@click.command(
    name="gitignore",
    help="List the gitignore templates available on GitHub"
)
def gitignore_cmd():
    if not get_current_user():
        click.echo(
            "You must be logged in to list gitignore templates",
            err=True
        )

        return

    user = get_current_user()

    list_gitignore_templates(user)


@click.command(
    name="repositories",
    help="List the repositories of a user"
)
@click.option(
    "--user",
    "-u",
    help="The user whose repositories to list; defaults to the logged in user",
    default=None
)
def repositories_cmd(user):
    if not user:
        user = get_current_user()

        if not user:
            click.echo(
                "You must be logged in to list repositories",
                err=True
            )

            return

    token = get_auth_token(user)

    if not token:
        click.echo(
            "You must be logged in to list repositories",
            err=True
        )

        return

    gh = Github(token)

    list_repositories(gh, user)


list_group.add_command(users_cmd)
list_group.add_command(licenses_cmd)
list_group.add_command(gitignore_cmd)
list_group.add_command(repositories_cmd)
