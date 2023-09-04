import sys

from github import Github

from ..utils import clone_repository as cr
from ..utils import get_auth_token


def clone_repository(option, opt_str, value, parser):
    token = get_auth_token()

    if len(value.split("/")) == 2:
        repoUser = value.split("/")[0]
        repoName = value.split("/")[1]
    else:
        repoUser = None
        repoName = value.split("/")[0]

    if token:
        gh = Github(token)
        user = gh.get_user()

        repoUser = user.login

        cr(repoUser, repoName)
    else:
        print("Please login first!")
        print("Run 'autorepo --login' to login.")
        print("Run 'autorepo --help' for more information.")

        sys.exit(1)


def list_repositories(option, opt_str, value, parser):
    token = get_auth_token()

    if token:
        gh = Github(token)
        user = gh.get_user()

        repos = '\n'.join(repo.name for repo in user.get_repos())

        print(repos)
    else:
        print("Please login first!")
        print("Run 'autorepo --login' to login.")
        print("Run 'autorepo --help' for more information.")

        sys.exit(1)
