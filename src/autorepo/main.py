#!/usr/bin/env -S python3 -B

import optparse
import sys

from .commands import (list_gitignore_templates, list_licenses,
                               list_repositories, login, logout)
from .utils import (clone_repository, create_repository,
                            initiate_repository)


def run():
    parser = optparse.OptionParser(usage="%prog [options] REPOSITORY_NAME")

    parser.add_option(
        '-l',
        '--login',
        action="callback",
        callback=login,
        help="Log in to your github account using access token."
    )

    parser.add_option(
        '--logout',
        '--logout',
        action="callback",
        callback=logout,
        help="Log out of your github account."
    )

    parser.add_option(
        '-r',
        '--repos',
        action="callback",
        callback=list_repositories,
        help="List all the repositories of the authenticated user."
    )

    parser.add_option(
        '--gitignore-templates',
        action="callback",
        callback=list_gitignore_templates,
        help="List all available gitignore templates."
    )

    parser.add_option(
        '--licenses',
        action="callback",
        callback=list_licenses,
        help="List all available licenses."
    )

    parser.add_option(
        '-d',
        '--description',
        dest="description",
        type="string",
        default="",
        help="Description of the repository to be created."
    )

    parser.add_option(
        '--lic',
        '--license',
        dest="license",
        type="string",
        default="mit",
        help="License to be used for the repository to be created."
    )

    parser.add_option(
        '--gitignore',
        dest="gitignore",
        type="string",
        default="",
        help="Gitignore template to be used for the repository to be created."
    )

    parser.add_option(
        '-p',
        '--private',
        dest="private",
        action="store_true",
        default=False,
        help="Make the repo private."
    )

    parser.add_option(
        '-e',
        '--existing',
        dest="existing",
        action="store_true",
        default=False,
        help="Connect with an existing repository."
    )

    (options, args) = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    if len(args) == 0:
        sys.exit(0)

    repoName = args[0]

    if options.existing:
        initiate_repository(
            create_repository(
                repoName,
                options.description,
                options.license,
                options.gitignore,
                options.private
            ),
            repoName
        )
    else:
        clone_repository(
            create_repository(
                repoName,
                options.description,
                options.license,
                options.gitignore,
                options.private
            ),
            repoName
        )
