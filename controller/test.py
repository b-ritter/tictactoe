import unittest
import random
import string
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
    
    def test_show_win(self):
        self.c.model.get_current_player_value.return_value = 'X'
        choice = random.choice(['y','n'])
        self.c.view.render.return_value = choice
        self.c.play_again = MagicMock()
        self.c.show_win()
        msg_data = {"player": "X"}
        self.c.view.render.assert_called_with(self.c.model.get_board(), msg_data=msg_data, state=g.WIN)
        self.c.play_again.assert_called_with(choice)
    
    def test_show_tie(self):
        choice = random.choice(['y','n'])
        self.c.view.render.return_value = choice
        self.c.play_again = MagicMock()
        self.c.show_tie()
        self.c.view.render.assert_called_with(self.c.model.get_board(), state=g.TIE)
        self.c.play_again.assert_called_with(choice)
    
    def test_show_quit(self):
        self.c.view.render.return_value = 'y'
        res = self.c.show_quit()
        self.assertEqual(res, g.EXIT)

        self.c.view.render.return_value = 'n'
        res = self.c.show_quit()
        self.assertEqual(res, g.PLAY)

        rand_input = random.choice([c for c in list(string.ascii_lowercase) if c not in ['y','n']])
        self.c.view.render.return_value = rand_input
        res = self.c.show_quit()
        self.assertEqual(res, g.QUIT)

    def test_play_again(self):
        res = self.c.play_again('y')
        self.c.model.reset.assert_called_once()
        self.assertEqual(res, g.PLAY)
        self.c.model.reset.reset_mock()
        
        res = self.c.play_again('n')
        self.assertEqual(res, g.EXIT)

        res = self.c.play_again('q')
        self.assertEqual(res, g.QUIT)

        self.c.model.check_for_win_or_tie.return_value = random.choice([g.TIE,g.WIN])
        res = self.c.play_again('F')
        self.assertIn(res, [g.TIE, g.WIN])
    
    def test_handle_move_quits(self):
        res = self.c.handle_move('q')
        self.assertEqual(res, g.QUIT)

    def test_handle_move_gets_help(self):
        res = self.c.handle_move('h')
        self.assertEqual(res, g.HELP)

    def test_handle_move_catches_invalid_input(self):
        self.c.model.is_move_cmd.return_value = False
        res = self.c.handle_move('invalid')
        self.assertEqual(res, g.INVALID_INPUT)

    def test_handle_move_parses_move(self):
        self.c.model.parse_move.return_value = 0, 0
        self.c.handle_move('a1')
        self.c.model.parse_move.assert_called_with('a1')

    def test_handle_move_catches_invalid_move(self):
        self.c.model.parse_move.return_value = 0, 0
        self.c.model.is_move_valid.return_value = False
        res = self.c.handle_move('occupied space')
        self.assertEqual(res, g.INVALID_MOVE)

    def test_handle_move_updates_board(self):
        self.c.model.parse_move.return_value = 0, 0
        self.c.model.get_current_player.return_value = 'X'
        self.c.handle_move('a1')
        self.c.model.update_board.assert_called_with(0,0,'X')

    def test_handle_move_detects_win_or_tie(self):
        result = random.choice([g.WIN, g.TIE])
        self.c.model.parse_move.return_value = 0, 0
        self.c.model.check_for_win_or_tie.return_value = result
        res = self.c.handle_move('winning or tying move')
        self.assertIn(res, [g.WIN, g.TIE])

    def test_handle_move_switches_players(self):
        self.c.model.current_player = 1
        self.c.model.switch_players.return_value = 0
        self.c.model.parse_move.return_value = 0, 0
        self.c.model.check_for_win_or_tie.return_value = g.PLAY
        res = self.c.handle_move('play on')
        self.assertEqual(res, g.PLAY)
        self.c.model.set_current_player.assert_called_with(0)


if __name__ == '__main__':
    unittest.main()