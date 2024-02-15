import toml

from config.sqllite_config import SqliteConfig


class SessionsConfig():
    def __init__(self,path_config:toml):
        self.sessions: dict = {}
        sqlite_session = SqliteConfig(path_config['flask']['sql_lite_database_uri']).get_session()

        self.sessions['sqlite_session'] = sqlite_session

    def get_all_sessions(self):
        return self.sessions