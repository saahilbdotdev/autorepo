import click

from ..utils import add_remote, clone_repo, create_repo, init_repo


@click.command(
    name="clone",
    help="Clone a repository"
)
@click.option(
    "--url",
    required=False,
    help="Repository clone url"
)
@click.option(
    "--user",
    "-u",
    help="User/Organization username"
)
@click.option(
    "--repo",
    "-r",
    help="Repository name"
)
def clone_cmd(url, user, repo):
    retcode = clone_repo(url, user, repo)

    if retcode is None or retcode != 0:
        click.echo("Failed to clone the repository", err=True)

        return

    click.echo("Repository cloned successfully")


@click.command(
    name="create",
    help="Create a repository and clone it"
)
@click.argument(
    "name",
    required=True
)
@click.option(
    "--no-clone",
    "-n",
    is_flag=True,
    default=False,
    help="Create the repository without cloning it"
)
@click.option(
    "--organization",
    "-o",
    default=None,
    help="Create the repository in an organization"
)
@click.option(
    "--private",
    "-p",
    is_flag=True,
    default=False,
    help="Create a private repository"
)
@click.option(
    "--existing",
    "-e",
    is_flag=True,
    default=False,
    help="Use an existing directory"
)
@click.option(
    "--description",
    "-d",
    default=None,
    help="Repository description"
)
@click.option(
    "--license",
    "-l",
    default="mit",
    help="License template"
)
@click.option(
    "--gitignore",
    "-g",
    default="Python",
    help="Gitignore template"
)
def create_cmd(
    name,
    no_clone,
    organization,
    private,
    existing,
    description,
    license,
    gitignore
):
    repo = create_repo(
        name,
        description,
        license,
        gitignore,
        organization,
        private
    )

    if repo is None:
        click.echo("Failed to create the repository", err=True)

        return

    if no_clone:
        click.echo("Repository created successfully")

        return

    if existing:
        retcode = init_repo()

        if retcode is None:
            click.echo("Failed to initialize the repository", err=True)

            return

        retcode = add_remote(repo.clone_url)

        if retcode is None:
            click.echo("Failed to add the remote", err=True)

            return

        click.echo("Repository created and initialized successfully")

        return

    retcode = clone_repo(repo.clone_url)

    if retcode is None or retcode != 0:
        click.echo("Failed to clone the repository", err=True)

        return

    click.echo("Repository created and cloned successfully")
