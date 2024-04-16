from copy import deepcopy
from string import Template
import itertools
from game.states import GameStates as g

class View:
    def __init__(self):
        self.board_template = self.load_board_template()

    def load_board_template(self):
        templ = None
        with open("./view/templates/board_format.txt") as f:
            data = f.read()
            templ = Template(data)
        return templ

    def transform_board(self, data):
        data_ = deepcopy(data)
        for i, row in enumerate(data_):
            for j, _ in enumerate(row):
                if data_[i][j] == 0:
                    data_[i][j] = '- '
                if len(data_[i][j]) == 1:
                    data_[i][j] += " "
        return data_

    def format_board(self, data):
        data_ = self.transform_board(data)
        labels = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
        data = itertools.chain(*data_)
        data_keys = zip(labels,data)
        data_dict = {k: v for k, v in data_keys}
        return self.board_template.substitute(data_dict)

    def get_input(self, msg):
        return input(msg)

    def print_board(self, data):
        print(data)
    
    def get_template(self, state, msg_data):
        if state == g.PLAY:
            t = Template("Player ${player}'s move: ")
            return t.substitute(msg_data)
        elif state == g.INVALID_MOVE:
            t = Template("Oops, that space is  occupied. Player ${player}'s move: ")
            return t.substitute(msg_data)
        elif state == g.WIN:
            t = Template("Player $player wins. Play again? Type y/n ")
            return t.substitute(msg_data)
        elif state == g.HELP:
            return "Valid moves. Enter q to quit. Enter any other key to continue."
        elif state == g.QUIT:
            return "Would you like to quit? Type y/n "
        elif state == g.TIE:
            return "It's a tie. Play again? Type y/n "

    def render(self, data, msg_data=None, state=None):
        self.print_board(self.format_board(data))
        result = None
        if state:
            result = self.get_input(self.get_template(state, msg_data))
        else:
            result = self.get_input(msg_data)
        return result