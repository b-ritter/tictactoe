import os

from model import Model
from controller import Controller
from view import View

class Game:

    def __init__(self):
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model, self.view)
        self.loop()

    def loop(self):
        state = "PLAY"
        while state != "WIN" or state != "TIE":
            os.system("clear")
            if state == "PLAY":
                state = self.controller.get_move()
            elif state == "INVALID_INPUT":
                state = self.controller.show_help()
            elif state == "INVALID_MOVE":
                state = self.controller.get_move()
            elif state == "WIN":
                state = self.controller.show_win()
            elif state == "TIE":
                state = self.controller.show_tie()
            elif state == "EXIT":
                exit()