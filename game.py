import os

from model import Model
from controller import Controller
from view import View

class GameState:
    def __init__(self):
        self.state_name = None
        self.state_val = None

class Game:

    def __init__(self):
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.controller)
        self.loop()
        self.state = GameState()

    def set_state(self, state):
        if state == "WIN":
            self.view.set_state("showing_winner")
            exit()
        if state == "TIE":
            self.view.set_state("showing_tie")
            exit()
        if state == "QUIT":
            exit()
        if state == "PLAY":
            os.system("clear")
            self.view.set_state("showing_board")
        if state == "HELP":
            os.system("clear")
            self.view.set_state("showing_help")
        
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
            self.set_state("PLAY")
            if self.state.state_name == "HELP":
                self.set_state("HELP")
            elif self.state.state_name == "TRY_AGAIN":
                self.set_state("PLAY")
            else:
                self.controller.update_board(res)
                result = self.controller.check_for_win_or_tie()
                self.set_state(result)
                self.controller.switch_players()