from github import Github
from pathlib import Path
import json

from .login import getToken

licensesPath = Path(f"{Path.home()}/.config/autorepo/licenses.json")


def listRepositories(option, opt_str, value, parser):
    token = getToken()

    if token:
        gh = Github(token)
        user = gh.get_user()
        repos = '\n'.join(repo.name for repo in user.get_repos())
        print(repos)


def listGitignoreTemplates(option, opt_str, value, parser):
    token = getToken()

    if token:
        gh = Github(token)
        print('\n'.join(gh.get_gitignore_templates()))


def listLicenses(option, opt_str, value, parser):
    global licensesPath

    licenses = {}
    maxNameLength = 0
    maxKeywordLength = 0

    if licensesPath.exists():
        f = licensesPath.open("r")
        data = json.load(f)
        f.close()

        maxNameLength = data['maxNameLength']
        maxKeywordLength = data['maxKeywordLength']
        licenses = data['licenses']
    else:
        token = getToken()

        if token:
            gh = Github(token)
            lics = gh.get_licenses()

            f = licensesPath.open("w")

            for license in lics:
                licenses[license.name] = license.key

                if len(license.name) > maxNameLength:
                    maxNameLength = len(license.name)

                if len(license.key) > maxKeywordLength:
                    maxKeywordLength = len(license.key)

            json.dump({'maxNameLength': maxNameLength,
                       'maxKeywordLength': maxKeywordLength,
                       'licenses': licenses}, f, indent=2)
            f.close()

    print(f"License{' ' * (maxNameLength - len('License') + 2)}| Keyword")
    print("-" * (maxNameLength + 2) + "+-" + "-" * maxKeywordLength)

    for license in licenses:
        print(
            f"{license}{(maxNameLength - len(license) + 2) * ' '}| {licenses[license]}")
