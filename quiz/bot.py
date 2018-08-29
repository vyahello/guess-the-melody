import os
import time
from quiz.bot.telebot import Bot, QuizBot
from telebot.types import Message

bot: Bot = QuizBot()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def find_file_ids(message: Message):
    bot.send_message(message.chat.id, message.text)
    for file in os.listdir('music/'):
        f = open('music/{}'.format(file), mode='rb')
        msg = bot.send_voice(message.chat.id, f)
        bot.send_message(message.chat.id, msg.file_id(), reply_to_message_id=msg.message_id())
        time.sleep(3)


if __name__ == '__main__':
    bot.polling(none_stop=True)
