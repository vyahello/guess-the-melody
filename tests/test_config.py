from quiz.config import Config


def test_config_token() -> None:
    assert Config.token == '676607913:AAHX9mdt54NpnXdturivR6KuS6lNbWDxDPM'


def test_config_db_name() -> None:
    assert Config.db_name == 'melody.db'


def test_config_shelve_name() -> None:
    assert Config.shelve_name == 'shelve'
