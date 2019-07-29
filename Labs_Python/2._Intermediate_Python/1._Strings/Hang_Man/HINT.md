# Hang Man Hints

[Go Back to Lab Description](./README.md)

Start off with the following variables.

- `secretWord` : Array of characters in the secret word.
- `rightGuesses` : Array of characters the user has guessed correctly.
- `wrongGuesses` : Array of characters the user has guessed incorrectly.
- `lives` : Amount of wrong guesses the user has left.

I additionally implemented an array that served the same purpose as a `set`, meaning it's an array with no repeating elements.

```
secretSet = []

for letter in secretWord:
    if letter not in secretSet:
        secretSet.append(letter)
```

I found it easiest to just write a function that takes a string, and places all the characters in my `secretWord` array and my `secretSet` array.

```
string = "pineapple" 

for letter in string:
    secretWord.append(letter)
    if letter not in secretSet:
        secretSet.append(letter)
```

Keep in mind, you can always use the `in` function or `not in` for checking if elements are in an array. This is really how you should be checking all your details.

```
if 'a' in secretWord:
    # Do Something
```

Once you have that down, its easy to just print the letter if it's in the user's guesses, or print an underscore if it isn't.

```
def printWord(secretWord, rightGuesses):
    string = ""
    for letter in secretWord:
        if letter in rightGuesses:
            string += letter
        else: 
            string += "_"
        string += " "
    return string
```

Same goes with checking if it's a right or wrong guess.

I made sure to check if the user's input is one character long.

I also made sure to `.lower()` all user input so that no issues arose with capital letters.

```
userInput = input("Guess a letter: ").lower()
```

[Go Back to Lab Description](./README.md)