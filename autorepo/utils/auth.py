import keyring


def get_auth_token(username: str) -> str | None:
    try:
        token = keyring.get_password("autorepo", f"gh_token_{username}")
    except Exception:
        return None

    return token


def token_exists(username: str) -> bool:
    return get_auth_token(username) is not None


def set_auth_token(username: str, token: str) -> bool:
    try:
        keyring.set_password("autorepo", f"gh_token_{username}", token)

        return True
    except Exception:
        return False


def delete_auth_token(username: str) -> bool:
    if not token_exists(username):
        return False

    try:
        keyring.delete_password("autorepo", f"gh_token_{username}")

        return True
    except Exception:
        return False


def set_current_user(username: str) -> bool:
    if not token_exists(username):
        return False

    try:
        keyring.set_password("autorepo", "current_user", username)

        return True
    except Exception:
        return False


def get_current_user() -> str | None:
    try:
        username = keyring.get_password("autorepo", "current_user")
    except Exception:
        return None

    return username


def delete_current_user() -> bool:
    try:
        keyring.delete_password("autorepo", "current_user")

        return True
    except Exception:
        return False


def list_users() -> list:
    try:
        users = keyring.get_password("autorepo", "all_users")
        if users == "" or users == " " or users is None:
            return []

        users = users.split(";")

        return users
    except Exception:
        return []


def add_user(username: str) -> bool:
    users = list_users()
    if username in users:
        return False

    users.append(username)

    try:
        keyring.set_password("autorepo", "all_users", ";".join(users))

        return True
    except Exception:
        return False


def remove_user(username: str) -> bool:
    users = list_users()
    if username not in users:
        return False

    users.pop(users.index(username))

    try:
        keyring.set_password("autorepo", "all_users", ";".join(users))

        return True
    except Exception:
        return False


def set_default_current_user() -> bool:
    users = list_users()
    if len(users) == 0:
        delete_current_user()

        return False

    return set_current_user(users[0])


if __name__ == "__main__":
    print(list_users())
    print(len(list_users()))
    print(get_current_user())
    print(delete_current_user())
    print(get_current_user())
