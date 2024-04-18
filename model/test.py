import unittest
from itertools import chain
from typing import cast
from model import model
from unittest.mock import patch, MagicMock
from game.states import GameStates as g

class TestModel(unittest.TestCase):

    def setUp(self):
        self.m = model.Model()
        self.m.board = self.get_board_with_named_spaces()

    def get_board_with_named_spaces(self):
        return cast(list[int|str],list(chain(*self.m.valid_moves)))
        
    def test_new_board(self):
        res = self.m.new_board()
        self.assertEqual(res, [0]*9)

    def test_is_full(self):
        self.m.board = [0,'X',0,0,0,0,0,0,0]
        res = self.m.is_full()
        self.assertFalse(res)

        self.m.board = ['X','X','O','O','X','X','O','X','X']
        res = self.m.is_full()
        self.assertTrue(res)

    def test_get_row(self):
        row_1 = self.m.get_row(0)
        self.assertEqual(row_1, ['a1','a2','a3'])
        row_2 = self.m.get_row(1)
        self.assertEqual(row_2, ['b1','b2','b3'])
        row_3 = self.m.get_row(2)
        self.assertEqual(row_3, ['c1','c2','c3'])

    def test_get_col(self):
        col_1 = self.m.get_col(0)
        self.assertEqual(col_1, ['a1','b1','c1'])
        col_2 = self.m.get_col(1)
        self.assertEqual(col_2, ['a2','b2','c2'])
        col_3 = self.m.get_col(2)
        self.assertEqual(col_3, ['a3','b3','c3'])

    def test_get_val(self):
        self.m.valid_moves
        for i in range(0,3):
            for j in range(0,3):
                val = self.m.get_val(i,j)
                self.assertEqual(val, self.m.valid_moves[i][j])

    def test_get_diag(self):
        diag_1 = self.m.get_diag(0)
        self.assertEqual(diag_1,['a1','b2','c3'])
        diag_2 = self.m.get_diag(-1)
        self.assertEqual(diag_2,['a3','b2','c1'])

    def test_set_val(self):
        with self.assertRaises(ValueError):
            self.m.set_val(3,1,"v")
        with self.assertRaises(ValueError):
            self.m.set_val(1,3,"v")
        for i in range(0,3):
            for j in range(0,3):
                self.m.set_val(i,j,"v")
        self.assertEqual(self.m.board, ["v"]*9)

    def test_get_board(self):
        board_clone = self.m.get_board()
        self.assertEqual(board_clone,self.m.valid_moves)

    def test_update_board(self):
        for i in range(0,3):
            for j in range(0,3):
                self.m.update_board(i,j,0)
        self.assertEqual(self.m.board, ["X"]*9)

        for i in range(0,3):
            for j in range(0,3):
                self.m.update_board(i,j,1)
        self.assertEqual(self.m.board, ["O"]*9)

    def test_check_grid(self):
        board_slice = ["X",0,"O"]
        self.assertFalse(self.m.check_grid(board_slice))

        board_slice = ["X","X","O"]
        self.assertFalse(self.m.check_grid(board_slice))

        board_slice = [0,0,0]
        self.assertFalse(self.m.check_grid(board_slice))

        board_slice = ["X","X","X"]
        self.assertTrue(self.m.check_grid(board_slice))

        board_slice = ["O","O","O"]
        self.assertTrue(self.m.check_grid(board_slice))

    def test_check_for_win(self):
        win1 = [
            ["X","X","X"],
            ["X","O","O"],
            ["O","X","O"]]
        self.m.board = list(chain(*win1))
        res = self.m.check_for_win()
        self.assertTrue(res)

        win2 = [
            ["O","X","X"],
            ["O","X","O"],
            ["X","O","O"]]
        self.m.board = list(chain(*win2))
        res = self.m.check_for_win()
        self.assertTrue(res)

        win3 = [
            ["X","O","X"],
            ["X","O","O"],
            ["X","O","O"]]
        self.m.board = list(chain(*win3))
        res = self.m.check_for_win()
        self.assertTrue(res)

        win4 = [
            ["X","O","X"],
            ["O","O","X"],
            ["O","X","X"]]
        self.m.board = list(chain(*win4))
        res = self.m.check_for_win()
        self.assertTrue(res)

        tie = [
            ["O","X","O"],
            ["O","X","O"],
            ["X","O","X"]]
        self.m.board = list(chain(*tie))
        res = self.m.check_for_win()
        self.assertFalse(res)

        incomplete = [
            ["O","X",0],
            ["O","X","O"],
            ["X","O","X"]]
        self.m.board = list(chain(*incomplete))
        res = self.m.check_for_win()
        self.assertFalse(res)

    def test_check_for_tie(self):
        tie = [
            ["O","X","O"],
            ["O","X","O"],
            ["X","O","X"]]
        self.m.board = list(chain(*tie))
        res = self.m.check_for_tie()
        self.assertTrue(res)

    def test_check_for_win_or_tie(self):
        self.m.check_for_tie = MagicMock()
        self.m.check_for_win = MagicMock()

        self.m.check_for_tie.return_value = False
        self.m.check_for_win.return_value = False
        res = self.m.check_for_win_or_tie()
        self.assertEqual(res,g.PLAY)

        self.m.check_for_tie.return_value = True
        self.m.check_for_win.return_value = False
        res = self.m.check_for_win_or_tie()
        self.assertEqual(res,g.TIE)

        self.m.check_for_tie.return_value = False
        self.m.check_for_win.return_value = True
        res = self.m.check_for_win_or_tie()
        self.assertEqual(res,g.WIN)

    def test_get_current_player_value(self):
        # Test the get_current_player_value function
        pass

    def test_get_current_player(self):
        # Test the get_current_player function
        pass

    def test_set_current_player(self):
        # Test the set_current_player function
        pass

    def test_switch_players(self):
        # Test the switch_players function
        pass

    def test_is_move_cmd(self):
        # Test the is_move_cmd function
        pass

    def test_parse_move(self):
        # Test the parse_move function
        pass

    def test_is_move_valid(self):
        # Test the is_move_valid function
        pass

    def test_reset(self):
        # Test the reset function
        pass

if __name__ == '__main__':
    unittest.main()