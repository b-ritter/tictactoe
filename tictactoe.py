# Tic tac toe
# each component should be thought of as its own container
# Use state machine for view
from copy import deepcopy
import os 

class Model:
    def __init__(self):
        # Could set current player as state variable
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]    
        
        self.player_map = ['X','Y']

        self.history = []

    def is_full(self):
        return all([all(row) for row in self.board])

    def get_row(self,rownum):
        return self.board[rownum]

    def get_col(self, colnum):
        return [
            self.board[0][colnum],
            self.board[1][colnum],
            self.board[2][colnum]
        ]

    def check_space(self,row,col):
        return self.board[row][col]

    def get_diag(self, start_col): 
        if start_col == 0:
            return [
                self.board[0][0],
                self.board[1][1],
                self.board[2][2] 
            ]
        else:
            return [
                self.board[0][2],
                self.board[1][1],
                self.board[2][0]
            ]
    
    def get_board(self):
        return self.board
    
    def update_board(self, row, col, player):
        self.history.append(self.board)
        self.board[row][col] = self.player_map[player]
    
class Player:
    def __init__(self, rep):
        self.rep = rep
    
    def get_rep(self):
        return self.rep
    
    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

class Controller:
    def __init__(self, model):
        self.model = model
        self.current_player_idx = 0
        self.players = (Player('X'), Player('O'))

        for idx, player in enumerate(self.players):
            player.set_symbol(model.player_map[idx])

        self.valid_moves = [
                ["a1", "a2", "a3"],
                ["b1", "b2", "b3"],
                ["c1", "c2", "c3"]
            ]
 
    def get_player(self, val):
        for player in self.players:
            if player.get_rep() == val:
                return player
    
    def check_grid(self, board_slice):
        if all(board_slice) and (board_slice[0] == board_slice[1] == board_slice[2]):
            return True
        return False
        
    def check_for_win(self):
        # Check rows and diagonals for all x or all o
        res = False
        for i in range(0,3):
            row = self.model.get_row(i)
            res = self.check_grid(row)
            if(res):
                return True 
        for i in range(0,3):
            col = self.model.get_col(i)
            res = self.check_grid(col)
            if(res):
                return True 
        for i in range(0,2):
            diag = self.model.get_diag(i)
            res = self.check_grid(diag)
            if(res):
                return True 
        return False
    
    def check_for_tie(self):
        if self.model.is_full():
            return True

    def check_for_win_or_tie(self):
        if self.check_for_tie():
            return "TIE"
        if self.check_for_win():
            return "WIN"
        return False
    def get_current_player(self):
        return self.current_player_idx
    
    def set_current_player(self, player_idx):
        self.current_player_idx = player_idx

    def get_player_rep(self, idx):
        player = self.players[idx]
        return player.get_rep()
    
    def get_current_player_rep(self):
        player_idx = self.get_current_player()
        return self.players[player_idx].get_rep()

    def switch_players(self):
        self.set_current_player(1) if self.get_current_player() == 0 else self.set_current_player(0)

    def is_move_cmd(self, move_cmd):
        return move_cmd in set([el for row in self.valid_moves for el in row])
        
    def parse_move(self, move_cmd):
        row, col = move_cmd[0], move_cmd[1]
        row_map = {'a': 0, 'b': 1, 'c': 2}
        col_map = {'1': 0, '2': 1, '3': 2}
        row = row_map.get(row)
        col = col_map.get(col)
        return row, col

    def get_move(self):
        res = input()
        if not self.is_valid_move(res): 
            return False
        else:
            return res 

    def is_valid_move(self, move_cmd):
        if not self.is_move_cmd(move_cmd):
            return False 
        row, col = self.parse_move(move_cmd)        
        if not self.model.check_space(row, col) == 0:
            return False
        return (row, col) 

    def get_board(self):
        return self.model.get_board()
    
    def update_board(self, res):
        # could this 'listen' for updates, like an observable?
        row, col = self.parse_move(res)
        player = self.get_current_player()
        self.model.update_board(row, col, player)

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

class Main:

    def __init__(self):
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.controller)
        self.loop()

    def loop(self):
        # Could track overall state
        winner_or_tie = False
        while not winner_or_tie:
            os.system("clear")
            self.view.set_state("showing_board")
            self.view.set_state("prompting_user")
            res = self.controller.get_move()
            if not res:
                self.view.set_state("showing_help")
            else:
                #breakpoint()
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

if __name__ ==  "__main__":
    Main()
