"""This package is used for a bot logic implementation."""
from bots.logic.check_answer import answer
from bots.logic.create_test import create_test
from bots.logic.menu import menu
from bots.logic.start import start

routers = (start, create_test, answer, menu)
