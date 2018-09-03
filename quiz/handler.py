import random
from quiz.bot.bot import Bot, QuizBot
from quiz.bot.message.user import UserMessage, BotUserMessage
from quiz.bot.navigation.keyboard import BotReplyKeyboard
from quiz.config import Config
from quiz.bot.storage.storage import Storage, MelodyStorage
from telebot.types import Message
from quiz.bot.tools.utils import Utils, ShelterUtils, GenerateBotKeyboardMarkUp
from quiz.types import Action

bot: Bot = QuizBot()


@bot.message_handler(commands=['start', 'help'])
def start(message: Message) -> None:
    user_msg: UserMessage = BotUserMessage(message)
    bot.send_message(user_msg.chat_id(), 'Hello this is a melody quiz game. Please choose /game option to start a game')


@bot.message_handler(commands=['game'])
def game(message: Message) -> None:
    chat_id: int = BotUserMessage(message).chat_id()
    data_base: Storage = MelodyStorage(Config)
    utils: Utils = ShelterUtils(Config)
    _, file_id, right_answer, wrong_answer = data_base.select_single(random.randint(1, utils.get_rows_count()))

    markup = GenerateBotKeyboardMarkUp(right_answer, wrong_answer).perform()
    bot.send_voice(chat_id, file_id, reply_markup=markup.keyboard())
    utils.set_user_game(chat_id, right_answer)
    data_base.close()


@bot.message_handler(func=lambda message: True)
def check_answer(message: Message) -> None:
    chat_id: int = BotUserMessage(message).chat_id()
    utils: Utils = ShelterUtils(Config)
    answer: int = utils.get_user_answer(chat_id)

    if not answer:
        bot.send_message(chat_id, 'Choose /game command to start the quiz melody game')
    else:
        hide_keyboard: Action = BotReplyKeyboard().remove()
        if message.text == answer:
            bot.send_message(chat_id, 'Correct! Try once more /game?', reply_markup=hide_keyboard.perform())
        else:
            bot.send_message(chat_id, 'Wrong answer! Try once more /game?',
                             reply_markup=hide_keyboard.perform())
        utils.finish_user_game(chat_id)
