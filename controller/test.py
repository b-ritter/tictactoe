import unittest
from controller import controller
from unittest.mock import patch
from game.states import GameStates as g

class TestController(unittest.TestCase):
    @patch('model.model.Model')
    @patch('view.view.View')
    def setUp(self, mock_model, mock_view):
        self.c = controller.Controller(mock_model, mock_view)

    def test_get_move(self):
        self.c.model.get_current_player_value.return_value = "X"
        self.c.model.get_board.return_value = "board"
        self.c.view.render.return_value = "a1"
        self.c.get_move()
        self.c.model.handle_move.assert_called_with("a1")

    def test_show_help(self):
        res = self.c.show_help()
        self.c.view.render.assert_called_with(self.c.model.valid_moves, state=g.HELP)
        self.assertEqual(res, g.PLAY)
    
    # def test_play_again(self, res):
    #     res = self.c.play_again()
if __name__ == '__main__':
    unittest.main()