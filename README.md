# AutoRepo

A simple, CLI-based tool for easier management of github repositories.

## Installation

- Run the following command to install AutoRepo.

```
$ pip install autorepo
```

## Usage

- After the installation is complete, you can run the following command to start AutoRepo (this will print the help message):

```
$ repo
```

- Using any command (displayed in the help message) requires you to first be logged in to your github account using an access token (this is a one-time thing). You can generate an access token by following the instructions [here](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).

```
$ repo --login
```

Or

```
$ repo -l
```

- After logging in, you can use any of the commands displayed in the help message.
- For example, to create a new repository on GitHub, and subsequently clone it, you can run the following command:

```
$ repo <repo_name> [OPTIONS]
```

- To list all the repositories created by the current logged in user, you can run the following command:

```
$ repo -r
```

- To clone a repository, you can run the following command:

```
$ repo -c <repo_name>
```

- Or if you are not the owner of that repository, you can run the following command:

```
$ repo -c "<repo_user>/<repo_name>"
```

- You can view all the available licenses using the following command:

```
$ repo --licenses
```

- You can view all the available gitignore templates using the following command:

```
$ repo --gitignore-templates
```

- To logout of your github account, you can run the following command:

```
$ repo --logout
```

- To view the help message, you can run the following command:

```
$ repo --help
```
