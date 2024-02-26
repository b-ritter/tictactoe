
class Model:
    def __init__(self):
        self.num_rows = 3
        self.num_cols = 3
        self.board = [0]*self.num_rows*self.num_cols

        self.player_map = ['X','Y']

        self.history = []

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
        self.history.append(self.board)
        self.set_val(row, col, self.player_map[player])