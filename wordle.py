import random as r

class Wordle():
    
    def __init__(self, word):
        self.word = list(word)
        self.box = ['white', 'white', 'white', 'white', 'white']

    def updateColors(self, x, astr):
        self.box[x] = astr

    def getColors(self):
        return self.box

    def checkAnswer(self, userGuess):
        self.guess = list(userGuess)
        self.box = ['white', 'white', 'white', 'white', 'white']
        
        # Set yellow boxes
        for i in range(5):
            for j in range(5):
                if self.guess[i] == self.word[j] and self.box[i] != 'green':
                    self.updateColors(i, 'yellow')
                    break

        # Set green/gray boxes
        for i in range(5):    
            if self.guess[i] == self.word[i]:
                self.updateColors(i, 'green')
            elif self.box[i] != 'yellow':
                self.updateColors(i, 'gray')


thisWordle = Wordle('bobby') #for random word

def game():
    g = 0
    guessed = False
    print(thisWordle.getColors())

    while g < 7 and not guessed:
        guess = input("Guess the word! ").lower()
        thisWordle.checkAnswer(guess)
        if thisWordle.getColors().count('green') == 5:
            guessed = True
        else:
            print(thisWordle.getColors())
            print("Not quite!")
        g += 1

    if guessed:
        print(thisWordle.getColors())
        print("You guessed it!")
    else:
        print("Out of tries! The word was:", ''.join(thisWordle.word))

if __name__ == "__main__":
    game()