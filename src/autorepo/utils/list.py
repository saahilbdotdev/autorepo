import click
from github import Github

from .auth import get_auth_token


def pretty_print_licenses(item_dict):
    max_name_length = 0
    max_keyword_length = 0

    for name, keyword in item_dict.items():
        if len(name) > max_name_length:
            max_name_length = len(name)

        if len(keyword) > max_keyword_length:
            max_keyword_length = len(keyword)

    click.echo(
        f"License{' ' * (max_name_length - len('License') + 2)}| Keyword"
    )
    click.echo(
        "-" * (max_name_length + 2) + "+-" + "-" * max_keyword_length
    )

    for name, keyword in item_dict.items():
        click.echo(
            f"{name}{' ' * (max_name_length - len(name) + 2)}| {keyword}"
        )


def pretty_print_repositories(item_dict):
    max_name_length = 0
    max_default_branch_length = 0
    max_forks_count_length = 0
    max_license_length = 12
    max_stars_length = 0
    max_visibility_length = 7

    for name in item_dict:
        if len(name) > max_name_length:
            max_name_length = len(name)

        if len(item_dict[name]["default_branch"]) > max_default_branch_length:
            max_default_branch_length = len(item_dict[name]["default_branch"])

        if len(str(item_dict[name]["forks_count"])) > max_forks_count_length:
            max_forks_count_length = len(str(item_dict[name]["forks_count"]))

        if len(str(item_dict[name]["stars"])) > max_stars_length:
            max_stars_length = len(str(item_dict[name]["stars"]))

    if len("Name") > max_name_length:
        max_name_length = len("Name")

    if len("Default Branch") > max_default_branch_length:
        max_default_branch_length = len("Default Branch")

    if len("Forks Count") > max_forks_count_length:
        max_forks_count_length = len("Forks Count")

    if len("License") > max_license_length:
        max_license_length = len("License")

    if len("Stars") > max_stars_length:
        max_stars_length = len("Stars")

    if len("Visibility") > max_visibility_length:
        max_visibility_length = len("Visibility")

    header = "Name" + " " * (max_name_length - len("Name") + 2) + "| "
    header += "Default Branch" + " " * (
        max_default_branch_length - len("Default Branch") + 2) + "| "
    header += "Forks Count" + " " * (
        max_forks_count_length - len("Forks Count") + 2) + "| "
    header += "License" + " " * (
        max_license_length - len("License") + 2) + "| "
    header += "Stars" + " " * (
        max_stars_length - len("Stars") + 2) + "| "
    header += "Visibility"

    click.echo(header)

    click.echo(
        "-" * (max_name_length + 2) + "+-" + "-" * (
            max_default_branch_length + 2) + "+-" + "-" * (
            max_forks_count_length + 2) + "+-" + "-" * (
                max_license_length + 2) + "+-" + "-" * (
                    max_stars_length + 2) + "+-" + "-" * (
                        max_visibility_length)
    )

    for name in item_dict:
        repo_str = name + " " * (max_name_length - len(name) + 2) + "| "
        repo_str += item_dict[name]["default_branch"] + " " * (
            max_default_branch_length - len(
                item_dict[name]["default_branch"]) + 2) + "| "
        repo_str += str(item_dict[name]["forks_count"]) + " " * (
            max_forks_count_length - len(
                str(item_dict[name]["forks_count"])) + 2) + "| "
        repo_str += item_dict[name]["license"] + " " * (
            max_license_length - len(item_dict[name]["license"]) + 2) + "| "
        repo_str += str(item_dict[name]["stars"]) + " " * (
            max_stars_length - len(str(item_dict[name]["stars"])) + 2) + "| "
        repo_str += item_dict[name]["visibility"]

        click.echo(repo_str)


def list_licenses():
    token = get_auth_token()

    if not token:
        click.echo(
            "You must be logged in to list licenses",
            err=True
        )

        return

    gh = Github(token)
    licenses = gh.get_licenses()

    names = [license.name for license in licenses]
    keys = [license.key for license in licenses]

    pretty_print_licenses(dict(zip(names, keys)))


def list_gitignore_templates():
    token = get_auth_token()

    if not token:
        click.echo(
            "You must be logged in to list gitignore templates",
            err=True
        )

        return

    gh = Github(token)
    gitignore_templates = gh.get_gitignore_templates()

    for template in gitignore_templates:
        click.echo(template)


def list_repositories(gh, user=None):
    repos = {}

    if user:
        try:
            repositories = gh.get_user(user).get_repos()
        except Exception:
            try:
                repositories = gh.get_organization(user).get_repos()
            except Exception:
                click.echo("Invalid user or organization", err=True)

                return
    else:
        repositories = gh.get_user().get_repos()

    for repository in repositories:
        repos[repository.full_name] = {
            "default_branch": repository.default_branch,
            "forks_count": repository.forks_count,
            "license": repository.license.key if repository.license else "NA",
            "stars": repository.stargazers_count,
            "visibility": repository.visibility
        }

    pretty_print_repositories(repos)
