from Domains import Board, AI


class UI:
    @staticmethod
    def PrintMenu():
        print("1. Start a new game")
        print("2. Continue the saved game")

    @staticmethod
    def check_input1(num):
        if num not in range(6):
            return False
        return True

    def NewGame(self):
        b = Board()
        print(b)
        ai = AI()
        while not b.isGameWon("O") and not b.isGameWon("X"):
            inp = 0
            while inp == 0:
                line = int(input("Choose line<<"))
                while not self.check_input1(line):
                    print("Invalid input!")
                    line = int(input("Choose line<<"))
                column = int(input("Choose column<<"))
                while not self.check_input1(column):
                    print("Invalid input!")
                    column = int(input("Choose column<<"))
                if b.board[line][column] == " ":
                    inp = 1
                else:
                    print("This space is already filled! Choose another one")
            symbol = input("Choose symbol<<")
            b.move(symbol, line, column)
            print(b, '\n')
            if b.isGameWon("X") or b.isGameWon("O"):
                print("You won!")
                break
            if b.NoSpacesLeft():
                print("You lost!")
                break
            ai.choose_random(b)
            print(b, '\n')
            if b.isGameWon("X") or b.isGameWon("O"):
                print("You won!")
                break
            if b.NoSpacesLeft():
                print("You lost!")
                break

            print("Do you want to save the game?")
            print("1.Yes")
            print("2.No")
            cmd = int(input("<<"))
            if cmd == 1:
                b.WriteToFile("OAC.txt")
                break

    def continue_game(self):
        b = Board()
        b.ReadFromFile("OAC.txt")
        print(b)
        ai = AI()
        while not b.isGameWon("O") and not b.isGameWon("X"):
            inp = 0
            while inp == 0:
                line = int(input("Choose line<<"))
                while not self.check_input1(line):
                    print("Invalid input!")
                    line = int(input("Choose line<<"))
                column = int(input("Choose column<<"))
                while not self.check_input1(column):
                    print("Invalid input!")
                    column = int(input("Choose column<<"))
                if b.board[line][column] == " ":
                    inp = 1
                else:
                    print("This space is already filled! Choose another one")
            symbol = input("Choose symbol<<")
            b.move(symbol, line, column)
            print(b, '\n')
            if b.isGameWon("X") or b.isGameWon("O"):
                print("You won!")
                break
            if b.NoSpacesLeft():
                print("You lost!")
                break
            ai.choose_random(b)
            print(b, '\n')
            if b.isGameWon("X") or b.isGameWon("O"):
                print("You won!")
                break
            if b.NoSpacesLeft():
                print("You lost!")
                break

            print("Do you want to save the game?")
            print("1.Yes")
            print("2.No")
            cmd = int(input("<<"))
            if cmd == 1:
                b.WriteToFile("OAC.txt")
                break

    def start(self):
        self.PrintMenu()
        mod = {'1': self.NewGame, '2': self.continue_game}
        cmd = input("Read command<<")
        while cmd not in mod:
            print("Invalid command!\n")
            cmd = input("Read command<<")
        mod[cmd]()


if __name__ == '__main__':
    ui = UI()
    ui.start()
