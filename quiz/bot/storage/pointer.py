from abc import ABC, abstractmethod
from sqlite3.dbapi2 import Cursor
from typing import List, Tuple
from quiz.bot.storage.connection import Conn


class Pointer(ABC):
    """Database pointer interface abstraction."""

    @abstractmethod
    def execute(self, command: str) -> Cursor:
        pass

    @abstractmethod
    def fetch_all(self, command: str) -> List[Tuple[str]]:
        pass


class DBPointer(Pointer):
    """Database pointer implementation."""

    def __init__(self, conn: Conn) -> None:
        self._conn: Conn = conn

    def execute(self, command: str) -> Cursor:
        return self._conn.cursor().execute(command)

    def fetch_all(self, command: str) -> List[Tuple[str]]:
        return self.execute(command).fetchall()