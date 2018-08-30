from abc import ABC, abstractmethod
from typing import List, Tuple, Type, Any
from quiz.config import Config
from quiz.bot.storage.connection import Conn, DBConn
from quiz.bot.storage.pointer import Pointer, DBPointer
from quiz.bot.storage.table import Table, DBTable


class Storage(ABC):
    """Abstract interface for a melody bot storage."""

    @abstractmethod
    def select_all(self) -> None:
        pass

    @abstractmethod
    def select_single(self, row_num: int) -> List[Tuple[str]]:
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
        self._table: Table = DBTable(config)
        self._conn: Conn = DBConn(config)
        self._pointer: Pointer = DBPointer(self._conn)

    def select_all(self) -> List[Tuple[str]]:
        with self._conn:
            return self._pointer.fetch_all('select * from {}'.format(self._table))

    def select_single(self, row_num: int) -> Tuple[Any]:
        with self._conn:
            return self._pointer.fetch_all('select * from {} where id is {}'.format(self._table, row_num))[0]

    def count_rows(self) -> int:
        return len(self.select_all())

    def close(self) -> None:
        self._conn.close()
