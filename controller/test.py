import unittest
from controller import controller
from unittest.mock import patch

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

if __name__ == '__main__':
    unittest.main()