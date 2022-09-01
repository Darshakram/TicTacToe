# Project 3 - Tic-Tac-Toe Simulator
# Name: Darcy Eliasi
# Instructor: S. Einakian
# Section: 11
# Functions tests comes here

import unittest
from tictactoeFuncs import *


class TestCases(unittest.TestCase):
    def test_check_rows(self):
        list = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        self.assertFalse(check_rows(list))

        list2 = ["X", "O", "O", "O", "X", "O", "X", "X", "X"]
        self.assertTrue(check_rows(list2))

        list3 = ["O", "O", "O", "X", "X", "O", "X", "O", "X"]
        self.assertTrue(check_rows(list3))

    def test_check_cols(self):
        list4 = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        self.assertFalse(check_cols(list4))

        list5 = ["X", "O", "O", "O", "X", "O", "X", "X", "X"]
        self.assertFalse(check_cols(list5))

        list6 = ["O", "O", "O", "X", "X", "O", "X", "O", "X"]
        self.assertFalse(check_cols(list6))

    def test_check_diags(self):
        list7 = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        self.assertTrue(check_diags(list7))

        list8 = ["X", "O", "O", "O", "X", "O", "X", "X", "X"]
        self.assertTrue(check_diags(list8))

        list9 = ["O", "O", "O", "X", "X", "O", "X", "O", "X"]
        self.assertFalse(check_diags(list9))

    def test_board_full(self):
        list10 = ["O", "X", "O", "X", "X", "O", "X", "O", "X"]
        self.assertTrue(board_full(list10))

        list11 = ["X", "O", "O", " ", "X", "O", " ", "X", "X"]
        self.assertFalse(board_full(list11))

        list12 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertFalse(board_full(list12))

    def test_check_win(self):
        list13 = ["O", "O", "O", "X", "X", " ", " ", " ", "X"]
        self.assertTrue(check_win(list13))

        list14 = [" ", "O", "X", "X", "O", " ", "X", "O", " "]
        self.assertTrue(check_win(list14))

        list15 = ["X", "O", " ", "O", "X", " ", " ", "O", "X"]
        self.assertTrue(check_win(list15))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
