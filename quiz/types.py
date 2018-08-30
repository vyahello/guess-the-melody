from abc import ABC, abstractmethod
from typing import Any


class ContextManager(ABC):
    """Abstract interface context manager."""

    @abstractmethod
    def __enter__(self) -> Any:
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class DictAccess(ABC):
    """Abstract interface for a dictionary access object."""

    @abstractmethod
    def __getitem__(self, item: Any) -> Any:
        pass

    @abstractmethod
    def __setitem__(self, key: Any, value: Any) -> None:
        pass

    @abstractmethod
    def __delitem__(self, key: Any) -> None:
        pass
