from game.states import GameStates as g

class Model:

    def __init__(self):
        self.num_rows = 3
        self.num_cols = 3
        self.board = self.new_board()

        self.current_player = 0

        self.players = ['X','O']

        self.valid_moves = [
                ["a1", "a2", "a3"],
                ["b1", "b2", "b3"],
                ["c1", "c2", "c3"]
                ]

    def new_board(self):
        return [0]*self.num_rows*self.num_cols

    def is_full(self):
        return all(self.board)

    def get_row(self,rownum):
        res = []
        start_idx = rownum * self.num_cols
        for col in range(self.num_cols):
           res.append(self.board[start_idx + col])
        return res

    def get_col(self, colnum):
        res = []
        for r in range(self.num_rows):
            res.append(self.board[r * self.num_rows + colnum])
        return res

    def get_val(self, row, col):
        # row, col are 0 indexed
        return self.board[row * self.num_rows + col]

    def get_diag(self, start_col):
        res = []
        if start_col == 0:
            col_idx = 0
            for r in range(self.num_rows):
                res.append(self.get_val(r, col_idx))
                col_idx += 1
        else:
            col_idx = self.num_cols - 1
            for r in range(self.num_rows):
                res.append(self.get_val(r, col_idx))
                col_idx -= 1
        return res

    def set_val(self, row, col, val):
        # Row, col are 0 indexed
        if (row >= self.num_rows) or (col >= self.num_cols):
            raise ValueError
        self.board[row * self.num_rows + col] = val

    def get_board(self):
        board = []
        for row in range(self.num_rows):
            cols = []
            for col in range(self.num_cols):
               cols.append(self.get_val(row, col))
            board.append(cols)
        return board
    
    def update_board(self, row, col, player):
        self.set_val(row, col, self.players[player])
    
    def check_grid(self, board_slice):
        if all(board_slice) and (board_slice[0] == board_slice[1] == board_slice[2]):
            return True
        return False
        
    def check_for_win(self):
        res = False
        for i in range(0,3):
            row = self.get_row(i)
            res = self.check_grid(row)
            if(res):
                return True 
        for i in range(0,3):
            col = self.get_col(i)
            res = self.check_grid(col)
            if(res):
                return True 
        for i in range(0,2):
            diag = self.get_diag(i)
            res = self.check_grid(diag)
            if(res):
                return True 
        return False
    
    def check_for_tie(self):
        if self.is_full():
            return True

    def check_for_win_or_tie(self):
        if self.check_for_tie():
            return g.TIE
        if self.check_for_win():
            return g.WIN
        return g.PLAY

    def get_current_player_value(self):
        return self.players[self.get_current_player()]

    def get_current_player(self):
        return self.current_player
    
    def set_current_player(self, player):
        self.current_player = player

    def switch_players(self):
        return 1 if self.get_current_player() == 0 else 0

    def is_move_cmd(self, move_cmd):
        return move_cmd in set([el for row in self.valid_moves for el in row])
        
    def parse_move(self, move_cmd):
        row, col = move_cmd[0], move_cmd[1]
        row_map = {'a': 0, 'b': 1, 'c': 2}
        col_map = {'1': 0, '2': 1, '3': 2}
        row = row_map.get(row)
        col = col_map.get(col)
        return row, col
    
    def is_move_valid(self, row, col):
        if self.get_val(row, col) == 0:
            return True
        else:
            return False

    def reset(self):
        self.board = self.new_board()