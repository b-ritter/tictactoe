import os

from model import Model
from controller import Controller
from view import View
from states import GameStates as g

class Game:

    def __init__(self):
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model, self.view)
        self.loop()

    def loop(self):
        state = g.PLAY
        while state != g.WIN or state != g.TIE:
            os.system("clear")
            if state == g.PLAY:
                state = self.controller.get_move()
            elif state == g.INVALID_INPUT:
                state = self.controller.show_help()
            elif state == g.HELP:
                state = self.controller.show_help()
            elif state == g.INVALID_MOVE:
                state = self.controller.get_move()
            elif state == g.WIN:
                state = self.controller.show_win()
            elif state == g.TIE:
                state = self.controller.show_tie()
            elif state == g.EXIT:
                exit()