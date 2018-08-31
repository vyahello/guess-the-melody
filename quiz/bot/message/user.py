from abc import ABC, abstractmethod
from telebot.types import Message


class UserMessage(ABC):
    """User message abstract interface."""

    @abstractmethod
    def chat_id(self) -> int:
        pass

    @abstractmethod
    def text(self) -> str:
        pass


class BotUserMessage(UserMessage):
    """User message implementation."""

    def __init__(self, message: Message) -> None:
        self._message = message

    def chat_id(self) -> int:
        return self._message.chat.id

    def text(self) -> str:
        return self._message.text
