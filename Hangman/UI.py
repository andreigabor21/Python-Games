from Controller import Controller
from Repository import Sentence
import sys


class UI:

    sentence = Sentence()
    try:
        sentence.verif_file("Sentences.txt")
    except ValueError as val:
        print(str(val))
        sys.exit()

    controller = Controller(sentence)
    controller.init_guess()
    print(controller.make_string())
    controller.SaveToFile()

    def play(self):
        while True:
            letter = input("Read letter<<")
            if self.controller.is_letter_ok(letter):
                self.controller.put_letter(letter)
                self.controller.SaveToFile()
            else:
                self.controller.hang_plus()
                self.controller.SaveToFile()
            print(self.controller.make_string())
            if self.controller.isWon():
                print("Game won!")
                break
            if self.controller.isLost():
                print("Game Lost!")
                break


if __name__ == '__main__':
    ui = UI()
    ui.play()