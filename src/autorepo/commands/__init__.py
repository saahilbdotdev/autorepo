import click

from .auth import login_cmd, logout_cmd
from .list import list_group
from .repo import clone_cmd, create_cmd


@click.group(
    help="A simple CLI tool for creating github repositories"
)
def autorepo():
    pass


autorepo.add_command(login_cmd)
autorepo.add_command(logout_cmd)
autorepo.add_command(list_group)
autorepo.add_command(clone_cmd)
autorepo.add_command(create_cmd)
