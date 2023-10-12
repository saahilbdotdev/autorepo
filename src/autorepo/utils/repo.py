import subprocess

import click
from github import Github

from .auth import get_auth_token


def clone_repo(url=None, user=None, repo=None):
    token = get_auth_token()

    gh = Github(token)

    if url:
        url = url.replace("https://", f"https://{token}@")
    elif repo:
        if user:
            try:
                gh.get_user(user)
            except Exception:
                try:
                    gh.get_organization(user)
                except Exception:
                    click.echo(
                        "The user/org provided does not exist",
                        err=True
                    )

                    return None
        else:
            user = gh.get_user().login

        try:
            repo = gh.get_repo(f"{user}/{repo}")
        except Exception:
            click.echo(
                "The repository provided does not exist",
                err=True
            )

            return None

        url = repo.clone_url
        url = url.replace("https://", f"https://{token}@")
    else:
        click.echo(
            "You must provide a url or a user/org and repo name",
            err=True
        )

        return None

    return subprocess.call(["git", "clone", url])


def create_repo(
    name,
    description,
    license,
    gitignore,
    organization=None,
    private=False
):
    token = get_auth_token()

    if not token:
        click.echo(
            "You must be logged in to create a repository",
            err=True
        )

        return None

    gh = Github(token)

    if organization:
        try:
            user = gh.get_organization(organization)
        except Exception:
            click.echo(
                "The organization provided does not exist",
                err=True
            )

            return None
    else:
        user = gh.get_user()

    repo = user.create_repo(
        name=name,
        description=description or name,
        private=private,
        license_template=license,
        gitignore_template=gitignore,
        auto_init=True
    )

    return repo


def init_repo():
    retcode = subprocess.call(["git", "init"])

    if retcode is None or retcode != 0:
        click.echo("Failed to initialize the repository", err=True)

        return None

    click.echo("Repository initialized successfully")

    return 0


def add_remote(url, name="origin"):
    retcode = subprocess.call(["git", "remote", "add", name, url])

    if retcode is None or retcode != 0:
        click.echo("Failed to add the remote", err=True)

        return None

    click.echo("Remote added successfully")

    return 0
