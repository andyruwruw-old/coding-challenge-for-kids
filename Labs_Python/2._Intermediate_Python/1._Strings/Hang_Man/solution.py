secretString = "pineapple"
secretWord = []
secretSet = []
wrongLetters = []
rightGuesses = []
lives = 8

for letter in secretString:
    secretWord.append(letter)
    if letter not in secretSet:
        secretSet.append(letter)

def printWord(secretWord, rightGuesses):
    string = ""
    for letter in secretWord:
        if letter in rightGuesses:
            string += letter
        else: 
            string += "_"
        string += " "
    return string

def printWrong(wrongLetters):
    string = "Wrong: "
    for letter in wrongLetters:
        string += letter
        string += " "
    return string

def checkWin(secretSet, rightGuesses):
    for letter in secretSet:
        if letter not in rightGuesses:
            return False
    return True

def printStatus(secretWord, rightGuesses, wrongLetters, lives):
    print("")
    print("You have", str(lives), "lives remaining to guess the word.")
    print(printWord(secretWord, rightGuesses))
    print(printWrong(wrongLetters))
    print("")

def printLoss(secretWord, rightGuesses, wrongLetters, lives):
    print("")
    print("You lost! The word was:")
    print(printWord(secretWord, secretWord))
    print(printWrong(wrongLetters))
    print("")

def printWin(secretWord, rightGuesses, wrongLetters, lives):
    print("")
    print("You won! With ", str(lives), "lives remaining.")
    print(printWord(secretWord, rightGuesses))
    print(printWrong(wrongLetters))
    print("")


print("Welcome to Hangman!")
while True:
    if lives == 0:
        printLoss(secretWord, rightGuesses, wrongLetters, lives)
        break

    elif checkWin(secretSet, rightGuesses):
        printWin(secretWord, rightGuesses, wrongLetters, lives)
        break

    printStatus(secretWord, rightGuesses, wrongLetters, lives)

    while True:
        userInput = input("Guess a letter: ").lower()

        if len(userInput) == 1:

            if userInput in rightGuesses or userInput in wrongLetters:
                print("You already guessed that!")
                print("")

            elif userInput in secretWord:
                print("Right!")
                rightGuesses.append(userInput)
                break

            else: 
                print("Wrong!")
                lives -= 1
                wrongLetters.append(userInput)
                break

        else:
            print("Not a valid input!")
    

    



