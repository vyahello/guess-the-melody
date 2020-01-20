from shelve import DbfilenameShelf, open
from typing import Type
from quiz.config import Config
from quiz.types import ContextManager, DictAccess


class Shelter(ContextManager, DictAccess):
    """Interface for bot shelter."""

    def __init__(self, config: Type[Config]) -> None:
        self._shelter: DbfilenameShelf = open(config.shelve_name)

    def __enter__(self) -> "Shelter":
        return self

    def __getitem__(self, item: str) -> int:
        return self._shelter[item]

    def __setitem__(self, key: str, value: int) -> None:
        self._shelter[key] = value

    def __delitem__(self, key: str) -> None:
        del self._shelter[key]

    def close(self) -> None:
        self._shelter.close()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
