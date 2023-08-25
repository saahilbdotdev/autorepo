import subprocess

from github import Github

from .keyring_utils import get_auth_token


def create_repository(name, description, license, gitignoreTemplate, isPrivate):
    token = get_auth_token()

    if token:
        print("Creating repository...")

        gh = Github(token)
        user = gh.get_user()

        user.create_repo(
            name=name,
            gitignore_template=gitignoreTemplate,
            license_template=license,
            description=description,
            auto_init=True,
            private=isPrivate
        )

        print(f"Successfully created repository '{name}'.")

        return user.login
    else:
        print("Please login first!")
        print("Run 'autorepo --login' to login.")
        print("Run 'autorepo --help' for more information.")

        return None


def clone_repository(username, repoName):
    print(
        f"\nRunning 'git clone https://github.com/{username}/{repoName}.git'\n"
    )

    subprocess.call(
        ["git", "clone", f"https://github.com/{username}/{repoName}.git"]
    )

    print(f"\nSuccessfully cloned repository '{repoName}'.")


def initiate_repository(username, repoName):
    print("\nRunning 'git init' ...\n")

    subprocess.call(["git", "init"])

    print(
        f"\nRunning 'git remote add origin https://github.com/{username}/{repoName}.git'\n"
    )

    subprocess.call(
        [
            "git", "remote", "add", "origin",
            f"https://github.com/{username}/{repoName}.git"
        ]
    )

    print("Successfully added remote.\n")
