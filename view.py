from copy import deepcopy

class View:
    data = None

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
        rep = f"""
     |     |     
  {data_[0][0]} |  {data_[0][1]} |  {data_[0][2]} 
_____|_____|_____
     |     |     
  {data_[1][0]} |  {data_[1][1]} |  {data_[1][2]} 
_____|_____|_____
     |     |     
  {data_[2][0]} |  {data_[2][1]} |  {data_[2][2]} 
     |     |     
"""
        return rep

    def prompt_next_move(self, player):
        return f"Player {player} choose your move: "

    def prompt_ok(self):
        return "Ok?"

    def show_valid_moves(self, moves):
        return f"""Incorrect input.\nProvide input corresponding to the following grid:
                {self.format_board(moves)}"""

    def render(self, data):
        print(self.format_board(data))