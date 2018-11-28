import random


class Word:
    def __init__(self):
        self.word = self.getword()
        wordToShow = ''
        self.wordToShow = ''
        for total in range(0, len(self.word)):
            wordToShow = wordToShow + '_'
        self.wordToShow = wordToShow

    def validateletterexists(self, letter):
        if letter in self.word and letter not in self.wordToShow:
            return True
        return False

    def getword(self):
        file = open('files/palavras.txt')
        words = file.read()
        word = words.split("\n")
        return word[random.randrange(0, len(word))]

    def getLetterPositions(self, letter):
        position = 0
        for character in self.word:
            if character == letter:
                self.changeValue(position, letter)
            position = position + 1

    def changeValue(self, position, letter):
        wordToShow = list(self.wordToShow)
        wordToShow[position] = letter
        self.wordToShow = ''.join(wordToShow)

    def checkFinal(self):
        if '_' in self.wordToShow:
            return False
        return True


class Board:
    def __init__(self):
        self.board = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========''', '''
        
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========''', '''
        
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========''', '''
        
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========''']

    def position(self, position):
        return self.board[position]


def main():
    game = Word()
    board = Board()
    count = 0
    while True:
        print(board.position(count))
        print(game.wordToShow)
        letter = input('Digite a letra\n')
        if game.validateletterexists(letter):
            print('certo')
            game.getLetterPositions(letter)
        else:
            count = count + 1
            print('errado')
        if count == 7 or game.checkFinal():
            print('Jogo Finalizado. Palavra: ', game.wordToShow)
            break


if __name__ == "__main__":
    main()
