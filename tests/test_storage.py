from quiz.bot.storage.storage import MelodyStorage
from quiz.config import Config


def test_storage_len_select_all() -> None:
    assert len(MelodyStorage(Config).select_all()) == 8


def test_storage_len_single_records() -> None:
    assert len(MelodyStorage(Config).select_single(1)) == 4


def test_storage_count_rows() -> None:
    assert MelodyStorage(Config).count_rows() == 8
