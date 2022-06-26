from github import Github
import subprocess

from .login import getToken


def createRepository(name, description, license, gitignoreTemplate, isPrivate):
    token = getToken()

    if token:
        print("Creating repository...")

        gh = Github(token)
        user = gh.get_user()
        user.create_repo(name=name, gitignore_template=gitignoreTemplate, license_template=license,
                         description=description, auto_init=True, private=isPrivate)

        print(f"Successfully created repository '{name}'.")

        return user.login


def cloneRepository(username, repoName):
    print(
        f"\nRunning 'git clone https://github.com/{username}/{repoName}.git'\n")
    subprocess.call(
        ["git", "clone", f"https://github.com/{username}/{repoName}.git"])

    print(f"\nSuccessfully cloned repository '{repoName}'.")


def initiateRepostiory(username, repoName):
    print("\nRunning 'git init' ...\n")
    subprocess.call(["git", "init"])

    print(
        f"\nRunning 'git remote add origin https://github.com/{username}/{repoName}.git'\n")
    subprocess.call(["git", "remote", "add", "origin",
                    f"https://github.com/{username}/{repoName}.git"])
    print("Successfully added remote.\n")
