from player import Player

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
        if not self.model.get_val(row, col) == 0:
            return False
        return (row, col) 

    def get_board(self):
        return self.model.get_board()
    
    def update_board(self, res):
        # could this 'listen' for updates, like an observable?
        row, col = self.parse_move(res)
        player = self.get_current_player()
        self.model.update_board(row, col, player)