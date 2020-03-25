from typing import Any
import click
from bprint import bprint
from quiz.handler import bot


@click.command()
@click.option("--key", "-k", help="Telegram bot api key")
def __main(run: bool, key: str, **kwargs: Any) -> None:
    """The program allows to run telegram bot application."""
    bprint("Running quiz bot (press ctrl+c to escape)")
    bot.polling(none_stop=True, **kwargs)


if __name__ == "__main__":
    __main()
