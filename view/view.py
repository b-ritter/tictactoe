from copy import deepcopy
from string import Template
import itertools

class View:
    def __init__(self):
        self.board_template = self.load_template()

    def load_template(self):
        templ = None
        with open("./view/board_format.txt") as f:
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

    def render(self, data, msg):
        self.print_board(self.format_board(data))
        result = self.get_input(msg)
        return result