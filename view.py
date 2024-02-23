from copy import deepcopy

class View:
    data = None

    def __init__(self, controller):
        self.controller = controller
        
    def set_state(self, state):
        if state == "showing_board":
            self.data = self.draw_board() 
        if state == "prompting_user":
            self.data = self.prompt_next_move()
        if state == "showing_winner":
            player = self.controller.get_player_rep(
                self.controller.get_current_player()
            )
            self.data = f"The winner is {player}"
        if state == "showing_tie":
            self.data = "It's a tie!"
        if state == "showing_help":
            self.data = self.show_valid_moves()
        self.render()

    def draw_board(self):
        board = self.controller.get_board()
        return self.format_board(board)

    def transform_board(self, data):
        data_ = deepcopy(data)
        for i, row in enumerate(data_):
            for j, _ in enumerate(row):
                if data_[i][j] == 0:
                    data_[i][j] = '- '
                for player in self.controller.players:
                    if player.get_symbol() == data_[i][j]:
                        data_[i][j] = f"{player.get_rep()} "
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

    def prompt_next_move(self):
        return f"Player {self.controller.get_current_player_rep()} choose your move: "

    def show_valid_moves(self):
        return f"""Incorrect input.\nProvide input corresponding to the following grid:
                {self.format_board(self.controller.valid_moves)}"""

    def render(self):
        print(self.data)