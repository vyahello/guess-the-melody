from abc import ABC, abstractmethod
from typing import Type
from quiz.config import Config


class Table(ABC):
    """Database table interface."""

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class DBTable(Table):
    """Database table implementation."""

    def __init__(self, config: Type[Config]) -> None:
        self._config = config

    def name(self) -> str:
        return self._config.db_name.split('.')[0]

    def __str__(self) -> str:
        return f"{self.name()}"
