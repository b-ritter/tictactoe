import unittest
from itertools import chain
from typing import cast
from model import model
from controller import controller
from view import view
from unittest.mock import patch, MagicMock
from game.states import GameStates as g

class TestGame(unittest.TestCase):

    def setUp(self):
        self.m = model.Model()
        self.v = view.View()
        self.c = controller.Controller(self.m, self.v)
    
    def test_x_wins(self):
        pass