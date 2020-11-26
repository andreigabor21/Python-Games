from termcolor import colored
from texttable import Texttable
import random


class Circle:
    def __init__(self, color):
        '''
        :param color: color of the circle
        '''
        self.color = color

    def __str__(self):
        return colored('●', str(self.color))


class Board:
    def __init__(self):
        '''
        Initializes the board as a matrix
        '''
        self.board = [['●' for j in range(7)] for i in range(6)]

    def __str__(self):

        # t = Texttable()
        # for i in range(6):
        #     row = self.board[i][:]
        #     t.add_row(row)
        # return t.draw()


        string = '---------------\n'
        for i in range(6):
            for j in range(7):
                string += '|'
                string += str(self.board[i][j])
            string += '|\n'
        string += '---------------\n'
        return string


    def move(self, circle, column):
        '''
        Make a move on the board
        :param circle: the color
        :param column: the column where will be the circle introduced
        :return: true if the move is possile, false otherwise
        '''
        i = 5
        while i >= 0:
            if self.board[i][column] == '●':
                self.board[i][column] = circle
                return True
            i -= 1
        return False

    def isWon(self):
        #horizontally
        for i in range(6):
            for j in range(4):
                if self.board[i][j] != '●':
                    if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3]:
                        return True
        #vertical
        for j in range(7):
            for i in range(3):
                if self.board[i][j] != '●':
                    if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j]:
                        return True
        #diagonal
        for i in range(3):
            for j in range(4):
                if self.board[i][j] != '●':
                    if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3]:
                        return True
        for i in range(3): #3,7
            j = 6
            while j >= 3:
                if self.board[i][j] != '●':
                    if self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3]:
                        return True
                j -= 1
        return False

    def isDraw(self):
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == '●':
                    return False
        return True


class Player:
    def __init__(self, circle: Circle):
        #the circle which the player will use
        self.circle = circle

    @property
    def get_circle(self):
        return self.circle

    def __str__(self):
        return "Player plays with " + str(self.get_circle)


class AI:
    def __init__(self, circle, oppcircle, difficulty):
        '''
        :param circle: the circle used by AI
        :param oppcircle: the circle used by human
        '''
        self.circle = circle
        self.oppcircle = oppcircle
        self.difficulty = difficulty

    @property
    def get_circle(self):
        return self.circle

    def isLegalMove(self, board: Board, column):
        i = 5
        while i >= 0:
            if board.board[i][column] == '●':
                return True
            i -= 1
        return False

    def available_move(self, board: Board):
        moves = []
        for column in range(7):
            if self.isLegalMove(board, column):
                moves.append(column)
        return moves

    def AI_Move(self, board: Board):
        board.move(self.get_circle, random.choice(self.available_move(board)))

    def __str__(self):
        return "AI plays with " + str(self.get_circle)

    def simulate_move(self, board: Board, column, circle: Circle):
        '''
        simulates a move for minimax
        :param board: the state of the board before the simulated move
        :param column: the column in which the move will be made
        :param circle: the circle(color) that will be introduced
        :return: a board in which the move was made
        '''
        board2 = Board()
        for i in range(6):
            for j in range(7):
                board2.board[i][j] = board.board[i][j]
        board2.move(circle, column)
        return board2

    def best_move(self, board: Board):
        '''
        Searches for the best move for a given state of the board
        :param board: the state of the board
        :return: the best move as a column
        '''
        legalmoves = {}
        for i in range(7):
            if self.isLegalMove(board, i):
                board2 = self.simulate_move(board, i, self.get_circle)
                legalmoves[i] = -self.find(self.difficulty - 1, board2, self.oppcircle)

        bestscore = -9999999
        bestmove = None
        moves = legalmoves.items()
        for move,score in moves:
            if score > bestscore:
                bestscore = score
                bestmove = move
        return bestmove

    def find(self, depth, board: Board, circle: Circle):
        '''
        Finds the score of a move by recursively completing a virtual board until
         the depth parameter is 0
        :param depth: the depth at which the board will be populated with moves
        :param board: the state of the board to find the score of a certain move
        :param circle: color
        :return: the score of the move calculated using an heuristic
        '''
        legalmoves = []
        for i in range(7):
            if self.isLegalMove(board, i):
                board2 = self.simulate_move(board, i, circle)
                legalmoves.append(board2)
        if depth == 0 or len(legalmoves) == 0 or board.isWon():
            return self.value(board, circle)
        if circle == self.circle:
            oppcircle = self.oppcircle
        else:
            oppcircle = self.circle

        score = -99999999
        for i in legalmoves:
            score = max(score, -self.find(depth - 1, i, oppcircle))
        return score

    def value(self, board, circle):
        '''
        Calculates the value for a configuration of the table using a certain heuristic
        :param board: the state of the board
        :param circle: color
        :return: the score of that configuration
        '''
        if circle == self.circle:
            oppcircle = self.oppcircle
        else:
            oppcircle = self.circle

        mfours = self.checkForConnection(board, circle, 4)
        mthrees = self.checkForConnection(board, circle, 3)
        mtwos = self.checkForConnection(board, circle, 2)
        ofours = self.checkForConnection(board, oppcircle, 4)
        othrees = self.checkForConnection(board, oppcircle, 3)
        otwos = self.checkForConnection(board, oppcircle, 2)
        if ofours > 0:
            return -100000
        else:
            return mfours * 100000 + mthrees * 100 + mtwos - othrees * 100 - otwos

    def checkForConnection(self, board: Board, circle: Circle, length):
        '''
        Calculates the number of connections of a given length
        :param board:
        :param circle: color
        :param length: the length of the connection
        :return: number of connections
        '''
        cont = 0
        for i in range(6):
            for j in range(7):
                if board.board[i][j] == circle:
                    cont += self.findVerConnection(i,j,board,length,board.board[i][j])
                    cont += self.findHorConnection(i,j,board,length,board.board[i][j])
                    cont += self.findDiagConnection(i,j,board,length,board.board[i][j])
        return cont

    def findVerConnection(self, i, j, board:Board, length, circle):
        '''
        number of vertical connections for a given position
        '''
        cont = 0
        if i + length - 1 <= 5:
            for x in range(length):
                if board.board[i + x][j] == circle:
                    cont += 1
                else:
                    break
        if cont == length:
            return 1
        else:
            return 0

    def findHorConnection(self, i, j, board:Board, length, circle):
        '''
        number of horizontal connections for a given position
        '''
        cont = 0
        if j + length - 1 <= 6:
            for x in range(length):
                if board.board[i][j + x] == circle:
                    cont += 1
                else:
                    x = length + 1
        if cont == length:
            return 1
        else:
            return 0

    def findDiagConnection(self, i , j, board:Board, length, circle):
        '''
        number of diagonal connections
        '''
        total = 0
        cont = 0
        if j + length - 1 < 7 and i + length - 1 < 6:
            for x in range(length):
                if board.board[i+x][j+x] == circle:
                    cont += 1
                else:
                    x = length + 1
        if cont == length:
            total += 1
        cont = 0
        if j + length - 1 < 7 and i - length + 1 >= 0:
            for x in range(length):
                if board.board[i-x][j+x] == circle:
                    cont += 1
                else:
                    x = length + 1
        if cont == length:
            total += 1
        return total
'''
b = Board()
c = Circle("blue")
c2 = Circle("red")
b.move(c,0)
b.move(c,1)
b.move(c,1)
b.move(c,2)
b.move(c,2)
b.move(c,2)
b.move(c2,3)
b.move(c,3)
b.move(c,3)
b.move(c,3)
b.move(c2,4)
print(b)
print(b.isWon())
'''