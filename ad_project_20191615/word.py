import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            word = line.strip()
            self.words.append(word)

    def randWord(self):
        r = random.randrange(self.words.__len__())
        return self.words[r]