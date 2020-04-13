[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Status](https://travis-ci.org/vyahello/guess-the-melody-bot.svg?branch=master)](https://travis-ci.org/vyahello/guess-the-melody-bot)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/guess-the-melody-bot/badge.svg?branch=master)](https://coveralls.io/github/vyahello/guess-the-melody-bot?branch=master)
[![Forks](https://img.shields.io/github/forks/vyahello/guess-the-melody-bot)](https://github.com/vyahello/guess-the-melody-bot/network/members)
[![Stars](https://img.shields.io/github/stars/vyahello/guess-the-melody-bot)](https://github.com/vyahello/guess-the-melody-bot/stargazers)
[![Issues](https://img.shields.io/github/issues/vyahello/guess-the-melody-bot)](https://github.com/vyahello/guess-the-melody-bot/issues)
[![GitHub watchers](https://img.shields.io/github/watchers/vyahello/guess-the-melody-bot.svg)](https://GitHub.com/vyahello/guess-the-melody-bot/graphs/watchers/)
[![GitHub contributors](https://img.shields.io/github/contributors/vyahello/guess-the-melody-bot.svg)](https://GitHub.com/vyahello/guess-the-melody-bot/graphs/contributors/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Guess the melody quiz
> Simple quiz telegram bot game written in **python**. 
> 
> It is called `GuessTheBot` so please check for it in the telegram application.

# Usage

![Usage](howto.gif)

## Tools
- python 3.6+
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- code analysis
  - [pytest](https://pypi.org/project/pytest/)
  - [flake8](http://flake8.pycqa.org/en/latest/)
  - [black](https://black.readthedocs.io/en/stable/)

## Usage
Run script from the root directory of the project:
```bash
python -m quiz
```
Please specify your telegram `API key` in [config.py](quiz/config.py) file to be able to use a bot.

## Development notes

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`) and unittests (`pytest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-code.sh
```

## Release notes

Please check [CHANGELOG](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Volodymyr Yahello_. Please check [AUTHORS](AUTHORS.md) to see all contributors.

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all dev project dependencies
