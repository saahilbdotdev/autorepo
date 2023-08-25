import json
from pathlib import Path

from github import Github

from ..utils import get_auth_token


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


def list_gitignore_templates(option, opt_str, value, parser):
    token = get_auth_token()

    if token:
        gh = Github(token)

        print('\n'.join(gh.get_gitignore_templates()))


def list_licenses(option, opt_str, value, parser):
    configPath = Path(f"{Path.home()}/.config/autorepo")
    licensesPath = Path(f"{str(configPath)}/licenses.json")

    licenses = {}
    maxNameLength = 0
    maxKeywordLength = 0

    if licensesPath.exists():
        with licensesPath.open("r") as f:
            data = json.load(f)

        maxNameLength = data['maxNameLength']
        maxKeywordLength = data['maxKeywordLength']

        licenses = data['licenses']
    else:
        configPath.mkdir()

        token = get_auth_token()

        if token:
            gh = Github(token)
            lics = gh.get_licenses()

            with licensesPath.open("w") as f:
                for license in lics:
                    licenses[license.name] = license.key

                    if len(license.name) > maxNameLength:
                        maxNameLength = len(license.name)

                    if len(license.key) > maxKeywordLength:
                        maxKeywordLength = len(license.key)

                json.dump(
                    {
                        'maxNameLength': maxNameLength,
                        'maxKeywordLength': maxKeywordLength,
                        'licenses': licenses
                    },
                    f,
                    indent=2
                )

    print(f"License{' ' * (maxNameLength - len('License') + 2)}| Keyword")
    print("-" * (maxNameLength + 2) + "+-" + "-" * maxKeywordLength)

    for license in licenses:
        print(
            f"{license}{(maxNameLength - len(license) + 2) * ' '}| {licenses[license]}"
        )
