import keyring


def get_auth_token():
    return keyring.get_password("autorepo", "gh_token")


def set_auth_token(token):
    keyring.set_password("autorepo", "gh_token", token)


def delete_auth_token():
    keyring.delete_password("autorepo", "gh_token")
