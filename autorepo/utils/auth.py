from autorepo.utils.config import Config


def get_auth_token(username: str) -> str | None:
    config = Config()

    if username not in config.users:
        return None

    token = config.users.get(username)

    return token


def token_exists(username: str) -> bool:
    config = Config()

    return config.users.get(username, "") != ""


def set_auth_token(username: str, token: str) -> None:
    config = Config()

    config.users[username] = token

    config.write_config()


def delete_auth_token(username: str) -> bool:
    config = Config()

    if username not in config.users:
        return False

    config.users[username] = ""

    config.write_config()

    return True


def set_current_user(username: str) -> bool:
    if not token_exists(username):
        return False

    config = Config()

    config.current_user = username

    config.write_config()

    return True


def get_current_user() -> str | None:
    config = Config()

    return config.current_user


def delete_current_user() -> bool:
    config = Config()

    if config.current_user == "":
        return False

    config.current_user = ""

    config.write_config()

    return True


def list_users() -> list:
    config = Config()

    return list(config.users.keys())


def add_user(username: str, token: str) -> bool:
    users = list_users()
    if username in users:
        return False

    set_auth_token(username, token)

    return True


def remove_user(username: str) -> bool:
    users = list_users()
    if username not in users:
        return False

    config = Config()

    config.users.pop(username)

    config.write_config()

    return True


def set_default_current_user() -> bool:
    users = list_users()
    if len(users) == 0:
        delete_current_user()

        return False

    return set_current_user(users[0])
