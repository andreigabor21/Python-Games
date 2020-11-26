import random

class Sentence:

    @staticmethod
    def verif_file(file_name):
        l = []
        f = open(file_name, "r")
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split()
            if len(line) == 0:
                raise ValueError("Not enough words!\n")
            for word in line:
                if len(word) < 3:
                    raise ValueError("There is a word too short! \n")
            l.append(line)
            line = f.readline().strip()
        f.close()
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i] == l[j]:
                    raise ValueError("Duplicate sentences! \n")

    def __init__(self):
        self._sentence = ""
        self._loadFromFile("Sentences.txt")

    def _loadFromFile(self, file_name):
        f = open(file_name, "r")
        '''
        lines = list(f.readlines())
        self._sentence = random.choice(lines)
        self._sentence.strip()
        f.close()
        '''
        lines = []
        line = f.readline().strip()
        while len(line) > 0:
            lines.append(line)
            line = f.readline().strip()
        self._sentence = random.choice(lines)
        f.close()

    def get_sentence(self):
        return self._sentence
