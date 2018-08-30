from abc import abstractmethod
from sqlite3.dbapi2 import Cursor, Connection, connect
from typing import Type
from quiz.config import Config
from quiz.types import ContextManager


class Conn(ContextManager):
    """Connection to database interface."""

    @abstractmethod
    def cursor(self) -> Cursor:
        pass


class DBConn(Conn):
    """Database connection implementation."""

    def __init__(self, config: Type[Config]) -> None:
        self._conn: Connection = connect(config.db_name)

    def __enter__(self) -> Conn:
        return self

    def cursor(self) -> Cursor:
        return self._conn.cursor()

    def close(self) -> None:
        self._conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
