from abc import ABC, abstractmethod


class Config(ABC):
    """Abstract interface for a bot config."""

    @abstractmethod
    def token(self) -> str:
        pass

    @abstractmethod
    def db_name(self) -> str:
        pass

    @abstractmethod
    def shelve_name(self) -> str:
        pass


class BotConfig(Config):
    """Bot config implementation."""

    def __init__(self) -> None:
        self._token: str = '676607913:AAHX9mdt54NpnXdturivR6KuS6lNbWDxDPM'
        self._db_name: str = 'music.db'
        self._shelve_name: str = 'shelve.db'

    def token(self) -> str:
        return self._token

    def db_name(self) -> str:
        return self._db_name

    def shelve_name(self) -> str:
        return self._shelve_name
