import random


class Word:
    def __init__(self):
        self.word = self.getword()

    def validateletterexists(self, letter):
        if letter in self.word:
            return True
        return False

    def getword(self):
        file = open('palavras.txt')
        words = file.read()
        word = words.split("\n")
        print(len(word))
        return word[random.randrange(0, len(word))]

    def getLetterPositions(self, letter):
        list = []
        count = 0
        for character in self.word:
            if character == letter:
                list.append(count)
            count = count + 1
        return list

class Board:
    def __init__(self, total):
        self.total = total



def main():
    game = Word()
    for quantity in range(0, 6):
        letter = input('Digite a letra\n')
        if game.validateletterexists(letter):
            print('certo')
            print(game.getLetterPositions(letter))
        else:
            print('errado')


if __name__ == "__main__":
    main()
