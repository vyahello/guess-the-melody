from abc import ABC, abstractmethod
from sqlite3 import Connection, connect
from typing import Type, List
from quiz.bot.config import Config


class Storage(ABC):
    """Abstract interface for a melody bot storage."""

    @abstractmethod
    def select_all(self) -> None:
        pass

    @abstractmethod
    def select_single(self, row_num: int) -> List:
        pass

    @abstractmethod
    def count_rows(self) -> int:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class MelodyStorage(Storage):
    """Represent melody bot storage."""

    def __init__(self, config: Type[Config]) -> None:
        self._connection: Connection = connect(config.db_name)
        self._cursor = self._connection.cursor()

    def select_all(self) -> None:
        with self._connection:
            self._cursor.execute('select * from music').fetchall()

    def select_single(self, row_num: int) -> List:
        with self._connection:
            return self._cursor.execute('select * from music where id = ?', (row_num,)).fetchall()[0]

    def count_rows(self) -> int:
        with self._connection:
            result = self._cursor.execute('select * from music').fetchall()
            return len(result)

    def close(self) -> None:
        self._connection.close()
