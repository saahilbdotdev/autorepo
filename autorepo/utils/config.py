from pathlib import Path
import json


class Config:
    def __init__(self):
        self.config_path = Path.joinpath(Path.home(), '.autorepo.config')
        self.current_user = ""
        self.users = {}

        if not self.config_path.exists():
            self.config_path.touch(mode=0o600, exist_ok=False)
            self.write_config()

        self.read_config()

    def read_config(self):
        with open(self.config_path, 'r') as f:
            config = json.load(f)

            self.current_user = config["current_user"]
            self.users = config["users"]

    def write_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    def to_dict(self):
        return {
            "current_user": self.current_user,
            "users": self.users,
        }
