import os

from model import Model
from controller import Controller
from view import View

class Game:

    def __init__(self):
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.controller)
        self.loop()

    def set_state(self, state):
        if state == "showing_winner":
            self.view.set_state("showing_winner")
        if state == "showing_tie":
            self.view.set_state("showing_tie")
    def loop(self):
        # Game states
        # * Prompting user to move
        # * Showing results of move
        # * Showing hint
        # * Prompting user to play again
        # * Showing results of finished game
        # * Display game result (win or tie)
        winner_or_tie = False
        while not winner_or_tie:
            os.system("clear")
            self.view.set_state("showing_board")
            self.view.set_state("prompting_user")
            res = self.controller.get_move()
            if not res:
                os.system("clear")
                self.view.set_state("showing_help")
                self.view.set_state("prompting_user")
                res = self.controller.get_move()
            else:
                self.controller.update_board(res)
                # Here we can implement controller states: play, win, tie
                result = self.controller.check_for_win_or_tie()
                if result:
                    winner_or_tie = result
                    os.system("clear")
                    self.view.set_state("showing_board")
                if result == "WIN":
                    self.view.set_state("showing_winner")
                    break
                elif result == "TIE":
                    self.view.set_state("showing_tie")
                    break
                self.controller.switch_players()