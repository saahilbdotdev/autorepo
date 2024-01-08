import keyring


def get_auth_token(username):
    return keyring.get_password("autorepo", f"gh_token_{username}")


def set_auth_token(username, token):
    keyring.set_password("autorepo", f"gh_token_{username}", token)


def delete_auth_token(username):
    keyring.delete_password("autorepo", f"gh_token_{username}")


def set_current_user(username):
    keyring.set_password("autorepo", "current_user", username)


def get_current_user():
    return keyring.get_password("autorepo", "current_user")


def token_exists(username):
    return get_auth_token(username) is not None


def list_users():
    users = keyring.get_password("autorepo", "all_users")
    if users is None:
        return []

    return users.split(";")


def add_user(username):
    users = list_users()
    if username in users:
        return

    users.append(username)

    keyring.set_password("autorepo", "all_users", ";".join(users))


def remove_user(username):
    users = list_users()
    if username not in users:
        return

    users.remove(username)

    keyring.set_password("autorepo", "all_users", ";".join(users))
