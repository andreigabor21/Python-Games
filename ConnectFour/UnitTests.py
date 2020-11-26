from unittest import TestCase
from Domains import *


class Tests(TestCase):

    def test_game(self):
        C1 = Circle('yellow')
        C2 = Circle('magenta')
        B = Board()
        B.board[5][0] = C1
        B.board[4][1] = C1
        B.board[3][2] = C1
        B.board[5][1] = C2
        B.board[5][2] = C2
        B.board[4][2] = C2
        B.board[2][2] = C2
        B.board[1][2] = C1
        B.board[0][2] = C2
        self.assertTrue(B.move(C1, 2) == False)
        self.assertTrue(B.move(C1, 0) == True)
        self.assertTrue(B.board[4][0] == C1)
        self.assertTrue(B.isWon() == False)
        self.assertTrue(B.isDraw() == False)
        B.move(C1, 0)
        B.move(C1, 0)
        self.assertTrue(B.isWon() == True)
