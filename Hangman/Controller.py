from Repository import Sentence


class Controller:
    hang = "hangman"
    count = 0

    def __init__(self, sentence: Sentence()):
        self.mysentence = sentence.get_sentence()
        self.guess = ["_"] * len(self.mysentence)
        self.hangman = ""

    #anna has apples -> a__a has a____s

    def init_guess(self):
        words = self.mysentence.split()
        for word in words:
            letter = word[0]
            letter2 = word[-1]
            for i in range(len(self.mysentence)):
                if letter == self.mysentence[i]:
                    self.guess[i] = letter
                elif letter2 == self.mysentence[i]:
                    self.guess[i] = letter2
            for i in range(len(self.mysentence)):
                if self.mysentence[i] == " ":
                    self.guess[i] = " "

    def is_letter_ok(self, letter):
        if letter in self.mysentence:
            return True
        return False

    def put_letter(self, letter):
        for i in range(len(self.mysentence)):
            if letter == self.mysentence[i]:
                self.guess[i] = letter


    def hang_plus(self):
        self.count += 1
        self.hangman = self.hang[:self.count]


    def isWon(self):
        for i in range(len(self.guess)):
            if self.guess[i] == "_":
                return False
        return True

    def isLost(self):
        if self.count == 7:
            return True
        return False

    def SaveToFile(self):
        s = ""
        for i in range(len(self.guess)):
            s += self.guess[i]
        s += " "
        s += self.hangman
        f = open("Result.txt", "w")
        f.write(s)
        f.close()

    def make_string(self):
        s = ""
        for chr in self.guess:
            s += chr + " "
        s += "  "
        s += self.hangman
        return s
