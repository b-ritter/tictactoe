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
        self.c.handle_move("a1")
        self.c.handle_move("b1")
        self.c.handle_move("a2")
        self.c.handle_move("b2")
        res = self.c.handle_move("a3")
        self.assertTrue(res == g.WIN and self.m.get_current_player_value() == 'X')

    def test_o_wins(self):
        self.c.handle_move("a1")
        self.c.handle_move("b1")
        self.c.handle_move("c2")
        self.c.handle_move("b2")
        self.c.handle_move("a3")
        res = self.c.handle_move("b3")
        self.assertTrue(res == g.WIN and self.m.get_current_player_value() == 'O')

    def test_tie(self):
        self.c.handle_move("a2")
        self.c.handle_move("a1")
        self.c.handle_move("b2")

        self.c.handle_move("a3")
        self.c.handle_move("c1")
        self.c.handle_move("b1")

        self.c.handle_move("c3")
        self.c.handle_move("c2")
        res = self.c.handle_move("b3") 
        self.assertTrue(res == g.TIE)
