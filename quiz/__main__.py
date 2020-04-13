from typing import Any
from bprint import bprint
from quiz.handler import bot


def __main(**kwargs: Any) -> None:
    """The program allows to run telegram bot application."""
    bprint("Running quiz bot (press ctrl+c to escape)")
    bot.polling(none_stop=True, **kwargs)


if __name__ == "__main__":
    __main()
