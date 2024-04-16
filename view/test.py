import unittest
from unittest.mock import MagicMock, patch
from view.view import View
from model.model import Model

class TestView(unittest.TestCase):
    def setUp(self):
        self.v = View()
        self.m = Model()

    @patch('view.view.View.get_input', return_value='a1')
    @patch('view.view.View.print_board', return_value='')
    @patch('view.view.View.format_board', return_value="formatted_board")
    def test_gets_input(self, mock_printer, mock_board, mock_input):
        b = mock_board()
        res = self.v.render(b, mock_input)
        self.assertEqual(res, mock_input())

    @patch('view.view.View.get_input', return_value='a1')
    @patch('view.view.View.print_board')
    @patch('view.view.View.format_board', return_value='formatted_board')
    def test_prints_board(self, mock_format_board, mock_print_board, mock_input):
        self.v.render(mock_format_board(), mock_input())
        mock_print_board.assert_called_with(mock_format_board())

    @patch('copy.deepcopy', return_value=[[0,0,0],["X","O","O"],[0,"X",0]])
    def test_transforms_board(self, mock_deepcopy):
        mock_val = mock_deepcopy()
        res = self.v.transform_board(mock_val)
        self.assertEqual([['- ','- ','- '],["X ","O ","O "],['- ',"X ",'- ']], res)

    def test_formats_board(self):
        formatted = self.v.format_board([['- ','- ','- '],["X ","O ","O "],['- ',"X ",'- ']])
        self.assertEqual(formatted,"""\
     |     |     
  -  |  -  |  -  
_____|_____|_____
     |     |     
  X  |  O  |  O 
_____|_____|_____
     |     |     
  -  |  X  |  - 
     |     |     \
""")
        
if __name__ == '__main__':
    unittest.main()