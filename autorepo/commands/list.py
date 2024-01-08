import click
from github import Github

from autorepo.utils import (get_auth_token, list_gitignore_templates,
                            list_licenses, list_repositories, list_users)


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

    if not users:
        click.echo("No users have logged in to autorepo")

        return

    click.echo("Users:\n")

    for user in users:
        click.echo(f"{user}\n")


@click.command(
    name="licenses",
    help="List the licenses available on GitHub"
)
def licenses_cmd():
    list_licenses()


@click.command(
    name="gitignore",
    help="List the gitignore templates available on GitHub"
)
def gitignore_cmd():
    list_gitignore_templates()


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
    token = get_auth_token()

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
