import pygame
import sys
from Domains import *
from Exception import GameLost, GameWon

pygame.init()
screen = pygame.display.set_mode((600,700))

b = Board()

def drawBoardGUI(board: Board):
    for i in range(6):
        for j in range(7):
            pass

while not b.isWon() and not b.isDraw():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("")

    '''
    def checkColumnInteger(cmd: str):
        if cmd.isdigit():
            column = int(cmd)
            if 0 < column < 8:
                return True
        return False
    def MenuDifficulty():
        print("Choose difficulty:")
        print("1. Easy")
        print("2. Normal")
        print("3. Hard")
        print("4. Very Hard")

    def Play(self):
        C1 = Circle("yellow")
        C2 = Circle("red")
        Player1 = Player(C1)
        self.MenuDifficulty()
        difficulty = int(input("<<"))
        diff = {1: 1, 2: 2, 3: 3, 4: 4}
        Robot = AI(C2, C1, diff[difficulty])
        B = Board()
        print(Player1)
        print(Robot)
        print(B)

        while not B.isDraw():
            col1 = input("Choose column<<")
            while not self.checkColumnInteger(col1):
                col1 = input("Choose a number between 1 and 7! <<")
            col1 = int(col1) - 1
            while not B.move(Player1.get_circle, col1):
                col1 = input("Choose a column which is not full! <<")
                while not self.checkColumnInteger(col1):
                    col1 = input("Choose a number between 1 and 7! <<")
                col1 = int(col1) - 1
            print(B)
            if B.isWon():
                raise GameWon
            if difficulty == 1:
                Robot.AI_Move(B)
            else:
                col2 = int(Robot.best_move(B))
                B.move(Robot.get_circle, col2)
            print(B)
            if B.isWon():
                raise GameLost
        if B.isDraw():
            print("Draw!")
        print('\n')
    '''