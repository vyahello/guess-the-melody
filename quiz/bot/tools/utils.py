from abc import ABC, abstractmethod
from random import shuffle
from typing import Type, Tuple
from telebot.types import ReplyKeyboardMarkup
from quiz.config import Config
from quiz.bot.storage.shelter import Shelter
from quiz.bot.storage.storage import Storage, MelodyStorage


class Utils(ABC):
    """Abstract interface for a bot utils."""

    @abstractmethod
    def count_rows(self) -> None:
        pass

    @abstractmethod
    def get_rows_count(self) -> int:
        pass

    @abstractmethod
    def set_user_game(self, chat_id: int, answer: int) -> None:
        pass

    @abstractmethod
    def finish_user_game(self, chat_id: int) -> None:
        pass

    @abstractmethod
    def get_user_answer(self, chat_id: int) -> int:
        pass


class ShelterUtils(Utils):
    """Shelter utils interface."""

    def __init__(self, config: Type[Config]) -> None:
        self._config = config
        self._db: Storage = MelodyStorage(config)

    def count_rows(self) -> None:
        with Shelter(self._config) as storage:
            storage['rows_count'] = self._db.count_rows()

    def get_rows_count(self) -> int:
        with Shelter(self._config) as storage:
            rows_num = storage['rows_count']
        return rows_num

    def set_user_game(self, chat_id: int, answer: int) -> None:
        with Shelter(self._config) as storage:
            storage[str(chat_id)] = answer

    def finish_user_game(self, chat_id: int) -> None:
        with Shelter(self._config) as storage:
            del storage[str(chat_id)]

    def get_user_answer(self, chat_id: int) -> int:
        with Shelter(self._config) as storage:
            try:
                return storage[str(chat_id)]
            except KeyError:
                pass


def generate_markup(right_answer: Tuple[str], wrong_answer: Tuple[str]) -> ReplyKeyboardMarkup:
    mark_up = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    all_answers: str = '{},{}'.format(right_answer, wrong_answer)

    list_items: list = [item for item in all_answers.split(',')]
    shuffle(list_items)

    for item in list_items:
        mark_up.add(item)
    return mark_up
