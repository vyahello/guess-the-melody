from abc import ABC, abstractmethod
from typing import Any
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from quiz.types import Action


class Keyboard(ABC):
    """Abstract interface for a bot keyboard."""

    @abstractmethod
    def markup(self) -> ReplyKeyboardMarkup:
        pass

    @abstractmethod
    def remove(self) -> ReplyKeyboardRemove:
        pass


class MarkUp(ABC):
    """Abstract interface for a keyboard markup."""

    @abstractmethod
    def add(self, item: str) -> None:
        pass

    @abstractmethod
    def keyboard(self) -> ReplyKeyboardMarkup:
        pass


class BotRemoveKeyboard(Action):
    """Bot keyboard removal implementation."""

    def __init__(self, selective: Any) -> None:
        self._remove: ReplyKeyboardRemove = ReplyKeyboardRemove(selective)

    def perform(self) -> ReplyKeyboardRemove:
        return self._remove


class BotReplyKeyboardMarkup(MarkUp):
    """Bot keyboard markup implementation."""

    def __init__(self, resize_keyboard: bool = None,
                 one_time_keyboard: bool = None,
                 selective: Any = None,
                 row_width: int = 3) -> None:

        self._markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard,
                                                                one_time_keyboard,
                                                                selective,
                                                                row_width)

    def keyboard(self) -> ReplyKeyboardMarkup:
        return self._markup

    def add(self, item: str) -> None:
        self._markup.add(item)


class BotReplyKeyboard(Keyboard):
    """Bot keyboard implementation."""

    def __init__(self, resize_keyboard: bool=True,
                 one_time_keyboard: bool=True,
                 selective: Any=None,
                 row_width: int=3) -> None:

        self._markup: MarkUp = BotReplyKeyboardMarkup(resize_keyboard,
                                                      one_time_keyboard,
                                                      selective,
                                                      row_width)
        self._remove: Action = BotRemoveKeyboard(selective)

    def markup(self) -> MarkUp:
        return self._markup

    def remove(self) -> Action:
        return self._remove
