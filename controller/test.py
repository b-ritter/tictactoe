import unittest
from controller import controller
from unittest.mock import patch, MagicMock
from game.states import GameStates as g

class TestController(unittest.TestCase):
    @patch('view.view.View')
    @patch('model.model.Model')
    def setUp(self, mock_model, mock_view):
        self.c = controller.Controller(mock_model, mock_view)

    def test_get_move(self):
        self.c.model.get_current_player_value.return_value = "X"
        self.c.model.get_board.return_value = "board"
        self.c.view.render.return_value = "a1"
        self.c.handle_move = MagicMock()
        self.c.get_move()
        self.c.handle_move.assert_called_with("a1")

    def test_show_help(self):
        res = self.c.show_help()
        self.c.view.render.assert_called_with(self.c.model.valid_moves, state=g.HELP)
        self.assertEqual(res, g.PLAY)
    
    def test_play_again(self):
        res = self.c.play_again('y')
        self.c.model.reset.assert_called_once()
        self.assertEqual(res, g.PLAY)
        self.c.model.reset.reset_mock()
        
        res = self.c.play_again('n')
        self.assertEqual(res, g.EXIT)

        res = self.c.play_again('q')
        self.assertEqual(res, g.QUIT)

        self.c.model.check_for_win_or_tie.return_value = g.TIE
        res = self.c.play_again('F')
        self.assertEqual(res, g.TIE)
    
    def test_handle_move_quits(self):
        pass

    def test_handle_move_gets_help(self):
        pass

    def test_handle_move_catches_invalid_input(self):
        pass

    def test_handle_move_parses_move(self):
        pass

    def test_handle_move_catches_invalid_move(self):
        pass

    def test_handle_move_detects_win_or_tie(self):
        pass

    def test_handle_move_switches_players(self):
        pass



if __name__ == '__main__':
    unittest.main()