'''UNIT TESTS

'''

import unittest
from board import Board

class TestBoardObj(unittest.TestCase):

    def setUp(self):
        self.fresh_board = Board()
        #self.filled_board = Board() todo : implement

    def test_dimensions(self):
        self.assertEqual(len(self.fresh_board.rows), 9)
        self.assertEqual(len(self.fresh_board.columns), 9)
        self.assertEqual(len(self.fresh_board.squares), 9)
   
    def test_empty_init(self):
        self.assertEqual(sum(self.fresh_board.rows), 0)
        self.assertEqual(sum(self.fresh_board.columns), 0)
        self.assertEqual(sum(self.fresh_board.squares), 0)
        
    def test_print(self):
        self.assertEqual()
