import click

from autorepo.commands.auth import (current_user_cmd, login_cmd, logout_cmd,
                                    switch_user_cmd)
from autorepo.commands.list import list_group
from autorepo.commands.repo import clone_cmd, create_cmd, delete_cmd


@click.group(
    help="A simple CLI tool for creating github repositories"
)
def autorepo():
    pass


autorepo.add_command(login_cmd)
autorepo.add_command(logout_cmd)
autorepo.add_command(current_user_cmd)
autorepo.add_command(switch_user_cmd)

autorepo.add_command(list_group)

autorepo.add_command(clone_cmd)
autorepo.add_command(create_cmd)
autorepo.add_command(delete_cmd)
