import os, random

# loads words from the file
def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()  # reads each line as a word
    return words

# displays the hangman image based on remaining lives
def showHangingMan(lives):
    images = [
    '''
_______
|     |
|     
|    
|     
|    
    ''',
    '''
_______
|     |
|     O
|    
|     
|    
    ''',
    '''
_______
|     |
|     O
|     |
|     
|    
    ''',
    '''
_______
|     |
|     O
|    /|
|     
|    
    ''',
    '''
_______
|     |
|     O
|    /|\\
|     
|    
    ''',
    '''
_______
|     |
|     O
|    /|\\
|    / 
|    
    ''',
    '''
_______
|     |
|     O
|    /|\\
|    / \\
|    
        '''
]
    print(images[6 - lives])  # display the image based on the remaining lives

# chooses a random word from the list
def chooseWord(wordList): return random.choice(wordList)

# clears the terminal screen for a new round
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# main game function
def runGame():
    clearTerminal()  # clear the terminal
    wordList = load_words('words.txt')  # load words from file
    word = chooseWord(wordList).upper()  # pick a random word and convert it to uppercase
    hiddenWord = ['_'] * len(word)  # create a list of underscores for each letter in the word

    # replace hyphens in the word (for hyphenated words)
    for i in range(len(word)):
        if word[i] == '-':
            hiddenWord[i] = '-'

    wrongLetters = []  # list of wrong letters guessed
    lives = 6  # initial number of lives

    print("Welcome to the Hangman Game! \n")

    # main game loop
    while lives > 0:
        showHangingMan(lives)  # display the hangman image
        print(" ".join(hiddenWord))  # display the hidden word with spaces between letters

        print(f"\nRemaining lives: {lives}")  # display remaining lives
        print(f"Wrong letters tried: {wrongLetters}")  # display the wrong letters guessed
        
        while True:
            letter = input("Type the desired letter: ").strip()  # prompt user for input
            # validate if it's a letter or a hyphen
            if (letter.isalpha() or letter == '-') and len(letter) == 1:
                break
            print("Please type a single letter (A-Z) or hyphen (-)")  # validation message

        letter = letter.upper()  # convert input to uppercase

        # check if the letter is in the word
        if letter not in word:
            lives -= 1  # lose a life if the letter is incorrect
            if letter not in wrongLetters:  # avoid adding the same wrong letter more than once
                wrongLetters.append(letter)
        else:
            # update the hidden word with the correct letter
            for i in range(len(word)):
                if word[i] == letter:
                    hiddenWord[i] = letter

            # check if the word has been fully revealed
            if "".join(hiddenWord) == word:
                print("Congratulations, you won!")  # victory message
                return

    showHangingMan(lives)  # display the final hangman image
    print(f"You ran out of lives. The word was {word}. Better luck next time!")  # loss message

runGame()  # start the game

