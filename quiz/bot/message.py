from abc import ABC, abstractmethod
from telebot.types import Message


class Voice(ABC):
    """Abstract interface for a bot voice message."""

    @abstractmethod
    def chat_id(self) -> int:
        pass

    @abstractmethod
    def file_id(self) -> str:
        pass

    @abstractmethod
    def message_id(self) -> int:
        pass


class VoiceMessage(Voice):
    """Represent voice message implementation."""

    def __init__(self, message: Message) -> None:
        self._message = message

    def chat_id(self) -> int:
        return self._message.chat.id

    def file_id(self) -> str:
        return self._message.voice.file_id

    def message_id(self) -> int:
        return self._message.message_id
