# AutoRepo

### AutoRepo is a simple, cli-based tool for creating github repositories, without leaving your terminal!

# Installation

- Run the following command to install autorepo:

```
$ pip install autorepo
```

Or

```
$ pipx install autorepo
```

# Usage

- After the installation is complete, you can run the following command to print the help message:

```
$ repo --help
```

- Using any command (displayed in the help message) requires you to first be logged in to your github account using a Personal Access Token (this is a one-time thing). You can generate a PAT by following the instructions <a href="https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/">here</a>:

```
$ repo login
```

- After logging in, you can create a new repository by running the following command:

```
$ repo create [OPTIONS] NAME
```

- To convert an existing project directory into a github repository, run the following command (the `-e` flag is used to specify that the directory contains an existing project):

```
$ cd <project_directory>
$ repo create -e [OPTIONS] NAME
```

- To logout of your github account, run the following command:

```
$ repo logout
```
