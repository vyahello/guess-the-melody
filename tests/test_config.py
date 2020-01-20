from quiz.config import Config


def test_config_token() -> None:
    assert Config.token == str()


def test_config_db_name() -> None:
    assert Config.db_name == "melody.db"


def test_config_shelve_name() -> None:
    assert Config.shelve_name == "shelve"
