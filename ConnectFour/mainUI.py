from UI import *

if __name__ == '__main__':
    Game = UI()
    try:
        Game.Play()
    except GameWon:
        print("You won!")
    except GameLost:
        print("You lost!")