import os

from model.model import Model
from controller.controller import Controller
from view.view import View
from game.states import GameStates as g

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
                state = self.controller.get_move(oops=True)
            elif state == g.WIN:
                state = self.controller.show_win()
            elif state == g.TIE:
                state = self.controller.show_tie()
            elif state == g.QUIT:
                state = self.controller.show_quit()
            elif state == g.EXIT:
                exit()