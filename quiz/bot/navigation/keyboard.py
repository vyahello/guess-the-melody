from abc import ABC, abstractmethod
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove


class ReplyKeyboard(ABC):
    """Abstract interface for an markup markup."""

    def __init__(self,  resize_keyboard=True, one_time_keyboard=True, selective=None, row_width=None) -> None:
        self._markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard,
                                                                one_time_keyboard,
                                                                selective,
                                                                row_width)
        self._remove = ReplyKeyboardRemove(selective)

    def markup(self) -> ReplyKeyboardMarkup:
        return self._markup

    def remove(self) -> ReplyKeyboardRemove:
        return self._remove
