from texttable import Texttable
import unittest
import random


class Board:
    def __init__(self):
        self.board = [[" " for j in range(6)] for i in range(6)]

    def __str__(self):
        t = Texttable()
        t.add_rows(self.board, [])
        return t.draw()

    def ReadFromFile(self, file_name):
        f = open(file_name, "r")
        lines = f.readlines()
        i = 0
        for line in lines:
            for j in range(6):
                if line[j] == "#":
                    self.board[i][j] = " "
                elif line[j] == "X":
                    self.board[i][j] = "X"
                elif line[j] == "O":
                    self.board[i][j] = "O"
            i += 1

    def WriteToFile(self, file_name):
        f = open(file_name, "w")
        for i in range(6):
            for j in range(6):
                if self.board[i][j] == " ":
                    f.write("#")
                else:
                    f.write(self.board[i][j])
            f.write('\n')

    def move(self, piece, i, j):
        self.board[i][j] = piece

    def isGameWon(self, piece):
        #check line
        for i in range(6):
            for j in range(2):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] == self.board[i][j+4] == piece:
                    return True
        #check columns
        for j in range(6):
            for i in range(2):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] == self.board[i+4][j] == piece:
                    return True
        #check diagonals
        if self.board[1][0] == self.board[2][1] == self.board[3][2] == self.board[4][3] == self.board[5][4] == piece:
            return True
        if self.board[0][1] == self.board[1][2] == self.board[2][3] == self.board[3][4] == self.board[4][5] == piece:
            return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] == self.board[4][4] == piece:
            return True
        if self.board[1][1] == self.board[2][2] == self.board[3][3] == self.board[4][4] == self.board[5][5] == piece:
            return True

        return False

    def NoSpacesLeft(self):
        for i in range(6):
            for j in range(6):
                if self.board[i][j] == " ":
                    return False
        return True

class AI:

    def checkForConnection(self, piece, board):
        pass

    def move(self, piece1, piece2, board):
        pass

    def available_moves(self,board : Board):
        l = []
        for i in range(6):
            for j in range(6):
                if board.board[i][j] == " ":
                    l.append((i,j))
        return l

    def choose_random(self, board: Board):
        symbol = random.choice(["X", "O"])
        elem = random.choice(self.available_moves(board))
        i = elem[0]
        j = elem[1]
        board.board[i][j] = symbol

'''
b = Board()
b.ReadFromFile("OAC.txt")
print(b)
'''