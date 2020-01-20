from typing import Any
import click
from bprint import bprint
from quiz.handler import bot


@click.command()
@click.option("--run", "-r", default=False, show_default=True, is_flag=True, help="Allows to run telegram bot app")
def main(run: bool, **kwargs: Any) -> None:
    """Runs telegram bot app."""
    if run:
        bprint("Running quiz bot (press ctrl+c to escape)")
        bot.polling(none_stop=True, **kwargs)
    else:
        bprint("Nothing to run.")


if __name__ == "__main__":
    main()
