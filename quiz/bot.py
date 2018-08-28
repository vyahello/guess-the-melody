from quiz.config import token
from telebot import TeleBot
from telebot.types import Message

bot: TeleBot = TeleBot(token=token)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def repeat_handler(message: Message) -> None:
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
